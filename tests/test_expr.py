from arbre.main import Noeud, Arbrebin, racine


def test_valeur():
    assert racine.valeur == "+"


def test_valeur_droite():
    assert racine.droit.valeur == 1
