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

G =[[1,5],[2,3],[5],[],[],[4]]
print(topological_sorting(G))