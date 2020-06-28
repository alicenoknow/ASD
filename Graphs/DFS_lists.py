def DFS_visit(G, s, u, parent):
    for n in G[u]:                      # sprawdzamy wszytkich sasiadow wierzcholka u
        if parent[n] is None and n != s:   # jesli nie byly jeszcze odwiedzone i nie sa wierzcholkiem poczatkowym
            parent[n] = u                  # przypisujemy im parent
            DFS_visit(G, s, n, parent)           # schodzimy nizej wywolujac DFS_visit dla n

def DFS( G ):
    v = len(G)                      # v - liczba wierzcholkow
    parent = [None]*v
    for u in range(v):              # sprawdzamy wszystkie wierzcholki
        if parent[u] is None:          # jesli jeszcze nie byly odwiedzone
            DFS_visit(G, u, u, parent)       # wywolujemy DFS_visit
    return parent


########################################################################################################################


def DFS_visit(G, s, u, visited):
    for n in G[u]:                              # sprawdzamy wszytkich sasiadow wierzcholka u
        if not visited[n]:                      # jesli nie byly jeszcze odwiedzone i nie sa wierzcholkiem poczatkowym
            visited[n] = True                   # przypisujemy im True
            DFS_visit(G, s, n, visited)         # schodzimy nizej wywolujac DFS_visit dla n

def DFS( G ):
    v = len(G)                                  # v - liczba wierzcholkow
    visited = [False]*v
    for u in range(v):                          # sprawdzamy wszystkie wierzcholki
        if not visited[u]:                      # jesli jeszcze nie byly odwiedzone
            DFS_visit(G, u, u, visited)         # wywolujemy DFS_visit
    return visited


'''
O(V + E)
'''