from app_core_tasca import App_tasques
from tasca import Tasca
import os, sys

sys.path.insert(0, __file__)
os.chdir(os.path.dirname(__file__))

def test_afegeix_tasca():
    app = App_tasques()
    tasca = Tasca(None, "comprar pa")
    app.afegeix_tasca(tasca)
    tasques = app.llegir_tasques()
    assert len(tasques) == 1
    assert tasques[0].titol == "comprar pa"

def test_modifica_tasca(depends=["test_afegeix_tasca"]):
    app = App_tasques()
    tasques = app.llegir_tasques()
    tasca = tasques[0]
    tasca.titol = "comprar llet"
    app.modifica_tasca(tasca)
    tasques = app.llegir_tasques()
    assert tasques[0].titol == "comprar llet"

def test_esborra_tasca(depends=["test_afegeix_tasca", "test_modifica_tasca"]):
    app = App_tasques()
    tasques = app.llegir_tasques()
    assert len(tasques) > 0
    for tasca in tasques:
        app.esborra_tasca(tasca.id)
    tasques = app.llegir_tasques()
    assert len(tasques) == 0
