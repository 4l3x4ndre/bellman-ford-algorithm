from math import inf as infinity
from graphe import GrapheMatPond

g = GrapheMatPond(6)
g.ajouter_arc(0, 1, 1)
g.ajouter_arc(1, 2, 4)
g.ajouter_arc(2, 3, 1)
g.ajouter_arc(3, 4, 20)
g.ajouter_arc(1, 4, 200)
g.ajouter_arc(0, 2, 50)
g.ajouter_arc(1, 5, 100)
g.ajouter_arc(5, 4, 1)


def bf(g, s):
    distances = [infinity] * len(g.sommets())
    distances[0] = 0

    for k in range(1, len(g.sommets())):
        sommet_courant = g.sommets()[k]
        for voisin in g.voisins(sommet_courant):
            distances[sommet_courant] = min(
                distances[sommet_courant],
                distances[voisin] + g.arc(voisin, sommet_courant)
            )

    return distances


d = bf(g, 0)
print(d)
