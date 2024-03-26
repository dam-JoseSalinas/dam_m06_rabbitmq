#!/usr/bin/python3
from tasca_persistencia import Tasca_persistencia

class Tasca_persistencia_rabbitmq(Tasca_persistencia):
    def __init__(self, host, queue, routing_key, exchange=''):
        self.host = host
        self._queue = queue
        self._routing_key = routing_key
        self._exange = exchange

    def desa(self, tasca):
        resultat = None
        missatge_body = { 
            "operacio": "desa", 
            "tasca" : str(tasca)
        }


        return resultat
    
    def get_list(self):
        resultat = []
        return resultat
    
    def modifica_tasca(self, tasca):
        resultat = None
        return resultat
    
    def esborra_tasca(self, id):
        pass