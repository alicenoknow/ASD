'''
directed graphs
1. DFS with saving time of discover
2. Sort vertices by time of discover in descending order
3. Reverse Edges
4. DFS, vertices taken in order of time of discover
'''

def DFS_time_visit(G, s, u, time, T):
    T += 1
    for n in G[u]:
        if time[n][1] is None and n != s:
           time[n][1] = T
           T = DFS_time_visit(G, s, n, time, T)
    return T


def DFS_time( G ):
    v = len(G)
    time = [[i, None] for i in range(v)]
    T = 0
    for u in range(v):
        if time[u][1] is None:
            time[u][1] = T
            T = DFS_time_visit(G, u, u, time, T)
    return time


def reverse_edges(G):
    newG = [[] for _ in range(len(G))]
    for v in range(len(G)):
        for u in G[v]:
            newG[u].append(v)
    return newG


def DFS_res_visit(G, s, u, visit):
    for n in G[u]:
        if visit[n] is False and n != s:
           visit[n] = True
           print(n, end=" ")
           DFS_res_visit(G, s, n, visit)


def DFS_res(G, vertices):
    v = len(G)
    visit = [False for _ in range(v)]
    for u in vertices:
        if visit[u] is False:
            visit[u] = True
            print("SCC: ", u, end=" ")
            DFS_res_visit(G, u, u, visit, )
            print()
    return


def sort_second(val):
    return val[1]


def SCC(G):
    time = DFS_time(G)
    time.sort(key=sort_second, reverse=True)
    rG = reverse_edges(G)
    vlist = []
    for i in time:
        vlist.append(i[0])
    DFS_res(rG, vlist)


G = [[2],
     [0],
     [1],
     [4],
     [5],
     [3, 1]]

SCC(G)