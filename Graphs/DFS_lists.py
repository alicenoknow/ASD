def DFS_visit(u, res):
    for n in G[u]:                      # sprawdzamy wszytkich sasiadow wierzcholka u
        if res[n] is None and n != 0:   # jesli nie byly jeszcze odwiedzone i nie sa wierzcholkiem poczatkowym
            res[n] = u                  # przypisujemy im parent
            DFS_visit(n, res)           # schodzimy nizej wywolujac DFS_visit dla n

def DFS( G ):
    v = len(G)                      # v - liczba wierzcholkow
    res = [None]*v
    for u in range(v):              # sprawdzamy wszystkie wierzcholki
        if res[u] is None:          # jesli jeszcze nie byly odwiedzone
            DFS_visit(u, res)       # wywolujemy DFS_visit
    return res


G = [[1,2],[0,2,3],[3,1,0],[]]          # elementarny test może wypisać np.
print( DFS(G) )                         # [None, 0, 1, 2]
