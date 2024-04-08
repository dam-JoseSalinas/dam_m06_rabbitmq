#!/usr/bin/python3

import flask
from app_core_tasca import App_core_tasca
from tasca import Tasca
import json
import sys,os

sys.path.insert(0, __file__)
os.chdir(os.path.dirname(__file__))

app = flask.Flask(__name__)
core_app = App_core_tasca()

#==========
# GET
#==========
@app.route("/tasks/", methods=["GET"])
def get_tasks():
    llista_jsons = []
    llista_tasques = core_app.llegir_tasques()
    for t in llista_tasques:
        tasca_json = str(t)                          # tasca_json -> str
        tasca_diccionary = json.loads(tasca_json)    # tasca_diccionary -> dictionary
        llista_jsons.append(tasca_diccionary)   # array de dictionaries
    return flask.jsonify(llista_jsons), 200     # retorna json + Content-type: application/json
#==========
# POST
#==========
@app.route("/tasks/", methods=["POST"])
def add_task():
    info_body = flask.request.get_data()    #info_body = '{"title": "hola"}' -> str
    tasca_nova = json.loads(info_body)      #tasca_nova = {"title": "hola"}  -> dictionary
    objecte_tasca = Tasca(None, tasca_nova["title"]) # Object.Tasca -> tasca.Tasca
    resultat = core_app.afegeix_tasca(objecte_tasca) #--> None
    return "", 204
#==========
# PUT
#==========
@app.route("/tasks/", methods=["PUT"])
def update_task():
    info_body = flask.request.get_data()    #info_body = '{"title": "hola"}' -> str
    tasca_nova = json.loads(info_body)      #tasca_nova = {"title": "hola"}  -> dictionary
    objecte_tasca = Tasca(
        None, tasca_nova["title"], 
        tasca_nova["done"], 
        tasca_nova["id"]
        ) # Object.Tasca -> tasca.Tasca
    resultat = core_app.modifica_tasca(objecte_tasca)
    return "", 204
#==========
# DELETE
#==========
@app.route("/tasks/<id>/", methods=["DELETE"])
def delete_task(id):
    resultat = core_app.esborra_tasca(id)
    return "", 204

app.run(
    host="0.0.0.0",
    debug=False)
