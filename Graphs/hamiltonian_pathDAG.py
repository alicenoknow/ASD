'''
dla DAG - directed acyclic graph
wywolaj DFS, jezeli wierzcholek zostal przetworzony leci na poczatek listy wynikowej
'''


def DFS_visit(sorted, G, u, visited):
    for n in G[u]:
        if visited[n] is False and n != 0:
            visited[n] = True
            DFS_visit(sorted, G, n, visited)
    sorted.insert(0,u)


def topological_sorting(G):
    v = len(G)
    sorted = []
    visited = [False]*v
    for u in range(v):
        if visited[u] is False:
            DFS_visit(sorted, G, u, visited)
    return sorted

def find_hamiltonian_path(G):
    Order = topological_sorting(G)
    return DFS(G, Order[0])





def DFS_visit2(G, s, u, visited):
    for n in G[u]:                      # sprawdzamy wszytkich sasiadow wierzcholka u
        if not visited[n]:   # jesli nie byly jeszcze odwiedzone i nie sa wierzcholkiem poczatkowym
            visited[n] = True                 # przypisujemy im parent
            DFS_visit2(G, s, n, visited)           # schodzimy nizej wywolujac DFS_visit dla n


def DFS( G , first):
    v = len(G)                      # v - liczba wierzcholkow
    visited = [False]*v
    u = first
    visited[u] = True
    DFS_visit2(G, u, u, visited)       # wywolujemy DFS_visit
    for i in range(v):
        if not visited[i]:
            return False
    return True



G =[[1],[2],[3,4],[4],[]]
print(find_hamiltonian_path(G))