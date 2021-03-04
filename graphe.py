class GraphMatrixWeighted:

    def __init__(self, n):
        self.adj = [[0] * n for _ in range(n)]
        self.n = n

    def add_edge(self, s1, s2, p):
        self.adj[s1][s2] = p
        self.adj[s2][s1] = p

    def edge_weight(self, s1, s2):
        return self.adj[s1][s2]

    def neighbours(self, s):
        l = []
        for i in range(len(self.adj[s])):
            if self.adj[s][i] != 0:
                l.append(i)
        return l

    def tops(self):
        return [x for x in range(self.n)]