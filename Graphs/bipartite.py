
def isBipartite(G, src):
        V = len(G)
        colorArr = [-1 for _ in range(V)]
        colorArr[src] = 1
        queue = []
        queue.append(src)
        while queue:

            u = queue.pop()
            if G[u][u] == 1:
                return False;

            for v in range(V):
                if G[u][v] == 1 and colorArr[v] == -1:
                    colorArr[v] = 1 - colorArr[u]
                    queue.append(v)
                elif G[u][v] == 1 and colorArr[v] == colorArr[u]:
                    return False
        return True



G = [[0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]]
print(isBipartite(G,0))
