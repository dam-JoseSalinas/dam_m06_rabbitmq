#!/usr/bin/python3

import app_core_tasca
import tasca
import json
import sys,os

sys.path.insert(0, __file__)
os.chdir(os.path.dirname(__file__))

core_app = app_core_tasca.App_tasques()

def neteja_pantalla():
    comanda = 'clear'
    if os.name == "nt":
        comanda = 'cls'
    os.system(comanda)


def mostra_menu():
    print("0. Sortir.")
    print("1. Mostra tasques.")
    print("2. Afegeix tasca.")
    print("3. Esborra tasca")


def get_tasques():
    return core_app.llegir_tasques()


def afegir_tasca():
    titol = input("Titol de la tasca: ")
    t = tasca.Tasca(None,titol)
    core_app.afegeix_tasca(t)


def esborrar_tasca(tasques):
    for t in tasques:
        print(f"{t.id}\t{t}")
    id_a_esborrar = int(input("Tria una tasca a esborrar: "))
    core_app.esborra_tasca(id_a_esborrar)

def procesa_opcio(opcio, llista_tasques):
    resultat = llista_tasques[::]
    if opcio == 1:
        resultat = get_tasques()
        for t in resultat:
            print(t)
    if opcio == 2:
        afegir_tasca()
        resultat = get_tasques()
    if opcio == 3:
        esborrar_tasca(resultat)
        resultat = get_tasques()
    return resultat


def main():
    opcio = None
    llista_tasques = get_tasques()
    while opcio != 0:
        mostra_menu()
        opcio = int(input("Tria una opcio: "))
        neteja_pantalla()
        llista_tasques = procesa_opcio(opcio, llista_tasques)

if __name__ == "__main__":
    main()