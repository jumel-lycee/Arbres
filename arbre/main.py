from graphviz import Digraph


class Noeud():

    """Voir la documentation de la classe dans le README"""

    def __init__(self):
        pass

    def __repr__(self):
        return str(self.valeur)

    def est_feuille(self):
        pass

    def cree_fils_gauche(self,valeur):
        pass

    def cree_fils_droit(self, valeur):
        pass


class Arbrebin:
    """Représente un objet arbre binaire
    - Propriétés : 
        * racine : objet de type Noeud désignant la racine de l'arbre
    - Méthodes :
        * show() : représentation graphique de l'arbre à l'aide de graphviz
    """

    def __init__(self, racine):
        self.racine = racine

    def show(self):
        """Renvoie un objet graphviz pour la visualisation graphique de l'arbre"""
        def representation(dot, noeud, aretes):
            # Ajoute la représentation du noeud à la représentation dot de l'arbre
            if noeud is not None:
                dot.node(str(id(noeud)), str(noeud.valeur))
                # Appel récursif de la fonction representation
                if noeud.gauche is not None:
                    representation(dot, noeud.gauche, aretes)
                    aretes.append((str(id(noeud)) , str(id(noeud.gauche))))
                if noeud.droit is not None:
                    representation(dot, noeud.droit, aretes)
                    aretes.append((str(id(noeud)) , str(id(noeud.droit))))

        dot = Digraph(comment="Arbre binaire", format='svg')
        aretes = []
        representation(dot, self.racine, aretes)
        dot.edges(aretes)
        return dot



racine = Noeud("A")
sous_arbre_gauche = racine.cree_fils_gauche("B")
sous_arbre_gauche.cree_fils_gauche("D")
racine.cree_fils_droit("C")

arbre = Arbrebin(racine)
arbre.show()
