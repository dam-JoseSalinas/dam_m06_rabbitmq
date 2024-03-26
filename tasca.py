#!/usr/bin/python3

import json

class Tasca():

    """
    tasca.py conté la classe Tasca que és la classe principal de la nostra aplicació.
    """
    # C O N S T R U C T O R
    def __init__(self, persistencia, titol, done=False, id=None):
        self._persistencia = persistencia
        self._titol = str(titol).strip()
        self._done = done
        self._id = id

    #persistencia
    @property
    def persistencia(self):
        return self._persistencia
    @persistencia.setter
    def persistencia(self, persistencia):
        self._persistencia = persistencia

    #titol
    @property
    def titol(self):
        return self._titol
    @titol.setter
    def titol(self, titol):
        self._titol = str(titol).strip()
    
    #done(status)
    @property
    def done(self):
        return self._done       
    @done.setter
    def done(self, done):
        self._done = done

    #id
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, valor):
        self._id = valor
    
    # M E T O D E S
    def desa(self):
        resultat = self._persistencia.desa(self)
        if resultat:
            self.id = resultat.id
        return resultat

    def __str__(self):
        resultat = {'id': self._id, 'titol': self._titol, 'done': self._done}
        return json.dumps(resultat)
    
    def __repr__(self):
        return self.__str__()
