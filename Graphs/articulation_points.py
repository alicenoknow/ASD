

def IS_POINT(a):
    print("Point: ", a)

def dfs(G, v, visited, low, time, p, T):
    children = 0
    visited[v] = True
    time[v] = low[v] = T
    T += 1
    for u in G[v]:
        if u == p:
            continue
        if visited[u]:
            low[v] = min(low[v], time[u])
        else:
            if v == p:
                children += 1
            T = dfs(G, u, visited, low, time, v, T)
            low[v] = min(low[v], low[u])
            if v != p and low[u] >= time[v]:
                IS_POINT(v)
    if children > 1:
        IS_POINT(v)
    return T

def find_points(G):
    T = 0
    n = len(G)
    visited = [False for _ in range(n)]
    low = [-1 for _ in range(n)]
    time = [-1 for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            T = dfs(G, i, visited, low, time, i, T)


G = [[1,6],
     [0,2],
     [1,3,6],
     [2,4,5],
     [3,5],
     [3,4],
     [0,2,7],
     [6]]

find_points(G)