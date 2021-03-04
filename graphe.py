class GrapheMatPond:
    """Un graphe représenté par une matrice d'adjacence,
       où les sommets sont les entiers $0, 1, ..., n - 1"""

    def __init__(self, n):
        self.adj = [[0] * n for _ in range(n)]
        self.n = n

    def ajouter_arc(self, s1, s2, p):
        self.adj[s1][s2] = p
        self.adj[s2][s1] = p

    def arc(self, s1, s2):
        return self.adj[s1][s2]

    def voisins(self, s):
        l = []
        for i in range(len(self.adj[s])):
            if self.adj[s][i] != 0:
                l.append(i)

        return l

    def sommets(self):
        return [x for x in range(self.n)]