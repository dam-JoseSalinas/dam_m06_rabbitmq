#!/usr/bin/python3
from factory_persistencia import Factory_persistencia
from tasca_persistencia_sqlite import Tasca_persistencia_sqlite

class Factory_persistencia_sqlite(Factory_persistencia):
    def __init__(self, ruta_fitxer):
        self.ruta_fitxer = ruta_fitxer

    def get_tasca_persistencia(self):
        return Tasca_persistencia_sqlite(self.ruta_fitxer)  