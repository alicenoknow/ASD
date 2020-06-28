class FU:
    def __init__(self, N):
        self.parent = [None for _ in range(N)]
        self.rank = [0 for _ in range(N)]

    def make_set(self, vertices):
        for vertice in range(vertices):
            self.parent[vertice] = vertice
            self.rank[vertice] = 0

    def find(self, vertice):
        if self.parent[vertice] != vertice:
            self.parent[vertice] = self.find(self.parent[vertice])
        return self.parent[vertice]

    def union(self, v1, v2):
            root1 = self.find(v1)
            root2 = self.find(v2)

            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1


def sort_third(val):
    return val[2]

def kruskal(v, edges):
    funion = FU(v)
    funion.make_set(v)
    edges.sort(key=sort_third)
    MST = []
    for edge in edges:
        v1, v2, w = edge
        if funion.find(v1) != funion.find(v2):
            funion.union(v1, v2)
            MST.append(edge)
    return MST

v = 7
edges = [[0,1,8],
         [0,4,5],
         [0,6,7],
         [1,2,6],
         [2,4,1],
         [2,3,2],
         [3,5,3],
         [4,5,2],
         [5,6,1]]
print(kruskal(v,edges))