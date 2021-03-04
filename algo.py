from math import inf
from graphe import GraphMatrixWeighted

g = GraphMatrixWeighted(6)
g.add_edge(0, 1, 1)
g.add_edge(1, 2, 4)
g.add_edge(2, 3, 1)
g.add_edge(3, 4, 20)
g.add_edge(1, 4, 200)
g.add_edge(0, 2, 50)
g.add_edge(1, 5, 100)
g.add_edge(5, 4, 1)


def belmannford(g, s):
    distances = [inf] * len(g.tops())
    distances[0] = 0

    for k in range(1, len(g.tops())):
        top = g.tops()[k]
        for neighbour in g.neighbours(top):
            distances[top] = min(
                distances[top],
                distances[neighbour] + g.edge_weight(neighbour, top)
            )

    return distances


d = belmannford(g, 0)
print(d)
