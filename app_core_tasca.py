#!/usr/bin/python3
from configurador import Configurador


class App_core_tasca():
    def __init__(self):
        factory_persistencia = Configurador.get_factory_persistencia()
        self._tasca_persistencia = factory_persistencia.get_tasca_persistencia()

    def afegeix_tasca(self, tasca_nova):
        tasca_nova.persistencia = self._tasca_persistencia
        tasca_nova.desa()

    def llegir_tasques(self):
        return self._tasca_persistencia.get_list()

    def modifica_tasca(self, tasca):
        return self._tasca_persistencia.modifica_tasca(tasca)
    
    def esborra_tasca(self, id):
        return self._tasca_persistencia.esborra_tasca(id)
    
