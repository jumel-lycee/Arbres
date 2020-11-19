# Arbres

Le but de ce TP est de construire une classe Arbre qui servira par la suite
à expérimenter diverses propriétés sur les arbres.

Chez vous, pensez à installer graphviz, avec pip :
```shell
python3 -m pip install graphviz
```

Le code proposé ici est incomplet et le répertoire tests permettra de
vérifier que votre implémentation correspond bien à la demande.

Un arbre binaire peut se représenter sous la forme de __Nœuds__ possédant
une valeur et un propriété gauche et droit correspondant à un sous arbre
gauche et un sous arbre droit.

Notre classe __Nœud__ disposera de 3 méthodes :
* **est_feuille()** qui renvoie une Vrai si l'objet est une feuille, faux
sinon
* **creer_feuille_gauche()** qui permet de créer une feuille à gauche avec la
valeur passée en paramètre
* **creer_feuille_droite()** qui permet de créer une feuille à droite avec la
valeur passée en paramètre

Pour les exemples, on regardera les tests.

