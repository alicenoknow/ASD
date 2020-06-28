'''
O(V + E)
'''
def DFS_visit(G, s, u, parent):
    for n in range(len(G[u])):                           # sprawdzamy wszytkich sasiadow wierzcholka u
        if G[u][n] == 1:
            if parent[n] is None and n != s:        # jesli nie byly jeszcze odwiedzone i nie sa wierzcholkiem poczatkowym
                parent[n] = u                       # przypisujemy im parent
                DFS_visit(G, s, n, parent)          # schodzimy nizej wywolujac DFS_visit dla n


def DFS( G, s):
    v = len(G)                                  # v - liczba wierzcholkow
    parent = [None]*v
    for u in range(v):                          # sprawdzamy wszystkie wierzcholki
        if parent[u] is None:                   # jesli jeszcze nie byly odwiedzone
            DFS_visit(G, u, u, parent)          # wywolujemy DFS_visit
    return parent


G = [[0, 1, 1, 0],
     [1, 0, 1, 1],
     [1, 1, 0, 1],
     [0, 0, 0, 0]]          # elementarny test może wypisać np.
print( DFS(G, 0) )                         # [None, 0, 1, 2]