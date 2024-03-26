#!/usr/bin/python3
from abc import ABC, abstractmethod

class Tasca_persistencia(ABC):

    @abstractmethod
    def desa(self, tasca):
        pass

    @abstractmethod
    def get_list(self):
        pass
    
    @abstractmethod
    def modifica_tasca(self, tasca):
        pass

    @abstractmethod    
    def esborra_tasca(self, id):
        pass
    