def linear(G):
    Q = [i for i in range(len(G))]
    out = True
    prev = Q.pop(0)
    while Q:
        curr = Q.pop(0)
        if G[prev][curr]:
            prev = curr
    for i in range(len(G)):
        if G[prev][i] != 0:
            out = False
            break
    for i in range(len(G)):
        if i!= prev and G[i][prev] != 1:
            out = False
            break
    if out:
        print("Uni out: ", prev)
    else:
        print("ni ma")


# ====================================================================================================


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
linear(G)