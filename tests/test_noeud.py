from arbre.main import Noeud


def test_racine():
    racine = Noeud("A")

    assert racine.valeur == "A"


def test_sous_arbre_gauche():
    racine = Noeud("A")
    sous_arbre_gauche = racine.cree_fils_gauche("B")
    sous_arbre_gauche.cree_fils_gauche("D")

    assert sous_arbre_gauche.gauche.valeur == "D"


def test_arbre():
    racine = Noeud("A")
    sous_arbre_gauche = racine.cree_fils_gauche("B")
    sous_arbre_gauche.cree_fils_gauche("D")
    racine.cree_fils_droit("C")

    assert not racine.est_feuille()


def test_arbre_droit():
    racine = Noeud("A")
    sous_arbre_gauche = racine.cree_fils_gauche("B")
    sous_arbre_gauche.cree_fils_gauche("D")
    racine.cree_fils_droit("C")

    assert racine.droit.est_feuille()


def test_arbre_gauche_valeur():
    racine = Noeud("A")
    sous_arbre_gauche = racine.cree_fils_gauche("B")
    sous_arbre_gauche.cree_fils_gauche("D")
    racine.cree_fils_droit("C")

    assert racine.gauche.valeur == "B"
