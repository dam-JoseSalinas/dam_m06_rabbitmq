#!/usr/bin/python3

import yaml
from factory_persistencia_sqlite import Factory_persistencia_sqlite
from factory_persistencia_rabbitmq import Factory_persistencia_rabbitmq

class Configurador:
    def get_configuracio():
        with open('configuracio.yml', 'r') as f:
            configuracio = yaml.load(f, Loader=yaml.SafeLoader)
        return configuracio
    
    def get_factory_persistencia():
        configuracio = Configurador.get_configuracio()
        if configuracio['motor'] == 'sqlite':
            return Factory_persistencia_sqlite(configuracio['ruta'])
        
        elif configuracio['motor'] == 'component':
            print("retornant configuracio component")
            return Factory_persistencia_rabbitmq(
                configuracio['host'], 
                configuracio['queue'], 
                configuracio['routing_key'])
        else:
            raise ValueError("No s'ha trobat la persistencia")
