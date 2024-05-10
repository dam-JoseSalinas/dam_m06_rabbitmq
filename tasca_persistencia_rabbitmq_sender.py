#!/usr/bin/python3
from tasca_persistencia import Tasca_persistencia
import pika
import json
import uuid
from tasca import Tasca

class Tasca_persistencia_rabbitmq_sender(Tasca_persistencia):
    def __init__(self, host, queue, routing_key, exchange=''):
        self._host = host
        self._queue = queue
        self._routing_key = routing_key
        self._exchange = exchange

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self._host))

    def desa(self, tasca):
        missatge_body = { 
            "operacio": "desa",
            "tasca" : str(tasca)
        }
        self.channel1 = self.connection.channel()
        self.channel1.queue_declare(queue=self._queue)

        self.channel1.basic_publish(exchange=self._exchange, routing_key=self._routing_key, body=json.dumps(missatge_body))
        #self.connection.close()
    
        resultat = None
        return resultat
    
    def get_list(self):
        self.channel2 = self.connection.channel()
        self.publish_queue = self.channel2.queue_declare(queue='', exclusive=True)
        self.callback_queue = self.publish_queue.method.queue

        # Poner en escucha
        self.channel2.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_recieve_response,
            auto_ack=True)
        
        self.response = None
        self.corr_id = None

        self.call()
        #self.connection.close()
        return self.response


    def call(self):
        missatge_body = { 
                "operacio": "llegeix"
        }
        self.corr_id = str(uuid.uuid4())
        self.channel2.basic_publish(
            exchange=self._exchange,
            routing_key=self._routing_key,
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=json.dumps(missatge_body))
        #on_recieve_response cambiara el valor
        while self.response is None:
            self.connection.process_data_events(time_limit=None)
        #return response 
    def on_recieve_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            response = []
            for t in json.loads(body):
                response.append(Tasca(None, t["titol"], t["done"], t["id"]))
            self.response = response
    
    
    def modifica_tasca(self, tasca):
        pass
    
    def esborra_tasca(self, id):
        pass