#!/usr/bin/python3

import yaml
from factory_persistencia_sqlite import Factory_persistencia_sqlite
from factory_persistencia_rabbitmq import Factory_persistencia_rabbitmq

class Configurador_db:
    def get_configuracio():
        with open('configuracio_db.yml', 'r') as f:
            configuracio = yaml.load(f, Loader=yaml.SafeLoader)
        return configuracio
    
    def get_factory_persistencia():
        configuracio = Configurador_db.get_configuracio()
        if configuracio['motor'] == 'sqlite':
            return Factory_persistencia_sqlite(configuracio['ruta'])
        
        else:
            raise ValueError("No s'ha trobat la persistencia")
