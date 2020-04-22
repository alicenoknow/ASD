def DFS_visit(G, u, res, color):
    for n in G[u]:                      # sprawdzamy wszytkich sasiadow wierzcholka u
        if res[n] == color and n != 0:   # jesli nie byly jeszcze odwiedzone i nie sa wierzcholkiem poczatkowym
            res[n] = u                  # przypisujemy im parent
            DFS_visit(n, res, )           # schodzimy nizej wywolujac DFS_visit dla n


def DFS( G ):
    v = len(G)                      # v - liczba wierzcholkow
    res = [None]*v
    color = 1
    for u in range(v):              # sprawdzamy wszystkie wierzcholki
        if res[u] != color:          # jesli jeszcze nie byly odwiedzone
            DFS_visit(G,u, res, 1)       # wywolujemy DFS_visit
        else: return False
    return res
