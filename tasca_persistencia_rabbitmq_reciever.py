import pika
from configurador_db import Configurador_db
from tasca import Tasca
import sys, os
import json
class Tasca_persistencia_rabbitmq_reciever:
    def __init__(self, host, queue, routing_key, exchange=''):
        self._host = host
        self._queue = queue
        self._routing_key = routing_key
        self._exchange = exchange
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self._host))
        self.channel = self.connection.channel()
    
    def operacio(self):
        self.channel.queue_declare(queue=self._queue)
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(queue=self._queue, on_message_callback=self.callback, auto_ack=False)
        #channel.basic_consume(queue=self._queue, on_message_callback=self.callback)
        self.channel.start_consuming()

    def callback(self, ch, method, props, body):
            factory_persistencia_db = Configurador_db.get_factory_persistencia()
            tasca_persistencia = factory_persistencia_db.get_tasca_persistencia()

            body = json.loads(body)
            operacio = body["operacio"]
            tasca = None

                
            #input("Enter para continuar o Ctrl+c para parar ejeccucion y hacer que el ack no se envie")
            
            if operacio == "desa":
                tasca = json.loads(body["tasca"])
                tasca_objecte = Tasca(tasca_persistencia, tasca["titol"])
                tasca_objecte.desa()
                ch.basic_ack(delivery_tag = method.delivery_tag)
                print(f"guardado: {tasca['titol']}")

            elif operacio == "llegeix":
                Tasca_list = tasca_persistencia.get_list()
                response = []
                for tasca in Tasca_list:
                    response.append(json.loads(str(tasca)))
                ch.basic_publish(exchange=self._exchange,
                                routing_key=props.reply_to,
                                properties=pika.BasicProperties(correlation_id = \
                                                                props.correlation_id),
                                body=json.dumps(response))
                ch.basic_ack(delivery_tag = method.delivery_tag)
                print("respuesta get_list: ", response)
    







if __name__ == "__main__":
    receiver = Tasca_persistencia_rabbitmq_reciever('localhost', 'operacio', 'operacio')
    try:
        receiver.operacio()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
