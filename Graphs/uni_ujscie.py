
def DFS_visit(G, s, u, parent):
    for n in range(len(G[u])):                           # sprawdzamy wszytkich sasiadow wierzcholka u
        if G[u][n] == 1:
            if parent[n] is 0 and n != s:        # jesli nie byly jeszcze odwiedzone i nie sa wierzcholkiem poczatkowym
                parent[n] = 1                       # przypisujemy im parent
                DFS_visit(G, s, n, parent)          # schodzimy nizej wywolujac DFS_visit dla n
            else:
                parent[n] += 1

def DFS( G, s):
    v = len(G)                                  # v - liczba wierzcholkow
    parent = [0]*v
    for u in range(v):                          # sprawdzamy wszystkie wierzcholki
        if parent[u] is 0:                   # jesli jeszcze nie byly odwiedzone
            DFS_visit(G, u, u, parent)          # wywolujemy DFS_visit
    return parent


def uni_out(G):
    arr = DFS(G,0)
    for i in range(len(arr)):
        if arr[i] == len(arr):
            print("Found: ", i)


G = [[0,0,1,0,0,0],
    [0,0,1,1,0,0],
    [0,0,0,0,0,0],
    [1,0,1,0,1,0],
    [0,0,1,0,0,1],
    [0,0,1,0,0,0]]

uni_out(G)