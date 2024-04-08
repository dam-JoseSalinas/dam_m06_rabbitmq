#!/usr/bin/python3
import tasca_persistencia
from tasca_persistencia_rabbitmq_sender import Tasca_persistencia_rabbitmq_sender
from factory_persistencia import Factory_persistencia

class Factory_persistencia_rabbitmq(Factory_persistencia):
    def __init__(self, host, queue, routing_key, exchange=''):
        self.host = host
        self._queue = queue
        self._routing_key = routing_key
        self._exchange = exchange

    def get_tasca_persistencia(self):
        return Tasca_persistencia_rabbitmq_sender(
            self.host, 
            self._queue, 
            self._routing_key, 
            self._exchange)