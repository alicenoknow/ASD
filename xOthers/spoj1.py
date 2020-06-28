def DFS_visit(G, s, u, parent):
    for n in G[u]:
        if parent[n] is None and n != s:
            parent[n] = u
            DFS_visit(G, s, n, parent)

def DFS( G ):
    v = len(G)
    cnt = 0
    parent = [None]*v
    for u in range(v):
        if parent[u] is None:
            cnt += 1
            DFS_visit(G, u, u, parent)
    return cnt



x = input().split(" ")
N = int(x[0])
M = int(x[1])
G = [[] for _ in range(N)]
cnt = 0

for i in range(M):
    x = input().split(" ")
    G[int(x[0])].append(int(x[1]))
    G[int(x[1])].append(int(x[0]))

print(DFS(G) - 1)


print(cnt)