def DFS_visit(G, s, u, visited, time):
    last = u
    last_time = time
    for n in G[u]:
        if not visited[n]:
            visited[n] = True
            last, last_time = DFS_visit(G, s, n, visited, time+1)
    return last, last_time


def diameter_of_tree(G):
    visited = [False for _ in range(len(G))]
    visited[0] = True
    far, time = DFS_visit(G, 0, 0, visited, 0)
    visited = [False for _ in range(len(G))]
    visited[far] = True
    far2, time = DFS_visit(G, far, far, visited, 0)
    print("from: ", far," to: ", far2," len: ", time)


G = [
    [1,2],
    [0],
    [0,3],
    [2]
]

diameter_of_tree(G)