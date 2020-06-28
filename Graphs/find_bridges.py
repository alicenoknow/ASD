

def IS_BRIDGE(a,b):
    print("Bridge: ", a, b)

def dfs(G, v, visited, low, time, p, T):
    visited[v] = True
    time[v] = low[v] = T
    T += 1
    for u in G[v]:
        if u == p:
            continue
        if visited[u]:
            low[v] = min(low[v], time[u])
        else:
            T = dfs(G, u, visited, low, time, v, T)
            low[v] = min(low[v], low[u])
            if low[u] > time[v]:
                IS_BRIDGE(v, u)
    return T

def find_bridges(G):
    T = 0
    n = len(G)
    visited = [False for _ in range(n)]
    low = [-1 for _ in range(n)]
    time = [-1 for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            T = dfs(G, i, visited, low, time, -1, T)


G = [[1,6],
     [0,2],
     [1,3,6],
     [2,4,5],
     [3,5],
     [3,4],
     [0,2,7],
     [6]]

find_bridges(G)