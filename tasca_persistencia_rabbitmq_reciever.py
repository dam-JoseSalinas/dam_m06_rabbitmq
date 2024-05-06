import pika
from configurador_db import Configurador_db
from tasca import Tasca
import json
import string
class Tasca_persistencia_rabbitmq_reciever:
    def __init__(self, host, queue, routing_key, exchange=''):
        self._host = host
        self._queue = queue
        self._routing_key = routing_key
        self._exchange = exchange

    def callback(self, ch, method, properties, body):
            factory_persistencia_db = Configurador_db.get_factory_persistencia()
            tasca_persistencia = factory_persistencia_db.get_tasca_persistencia()
            body = json.loads(body)
            tasca = json.loads(body["tasca"])
            operacio = body["operacio"]
            tasca_objecte = None
            if len(tasca) > 0:
                tasca_objecte = Tasca(tasca_persistencia, tasca["titol"])
            if operacio == "desa":
                tasca_objecte.desa()
            print("guardado")
    def operacio(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=self._host))
        channel = connection.channel()
        channel.queue_declare(queue=self._queue)
        channel.basic_consume(queue=self._queue, on_message_callback=self.callback, auto_ack=True)
        channel.start_consuming()
if __name__ == "__main__":
    receiver = Tasca_persistencia_rabbitmq_reciever('localhost', 'desa', 'desa')
    try:
        receiver.operacio()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)