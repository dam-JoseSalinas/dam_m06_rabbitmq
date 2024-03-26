#!/usr/bin/python3

from abc import ABC, abstractmethod

class Factory_persistencia(ABC):
    
    @abstractmethod
    def get_tasca_persistencia(self):
        pass