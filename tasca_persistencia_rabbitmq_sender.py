#!/usr/bin/python3
from tasca_persistencia import Tasca_persistencia
import pika
import json

class Tasca_persistencia_rabbitmq_sender(Tasca_persistencia):
    def __init__(self, host, queue, routing_key, exchange=''):
        self._host = host
        self._queue = queue
        self._routing_key = routing_key
        self._exchange = exchange

    def desa(self, tasca):
        missatge_body = { 
            "operacio": "desa",
            "tasca" : str(tasca)
        }

        connection = pika.BlockingConnection(pika.ConnectionParameters(host=self._host))
        channel = connection.channel()
        channel.queue_declare(queue=self._queue)

        channel.basic_publish(exchange=self._exchange, routing_key=self._routing_key, body=json.dumps(missatge_body))
        connection.close()
    
        resultat = None
        return resultat
    
    def get_list(self):
        pass
    
    def modifica_tasca(self, tasca):
        pass
    
    def esborra_tasca(self, id):
        pass