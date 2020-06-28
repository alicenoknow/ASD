import heapq


def prim(G, src):
    n = len(G)
    dist = [[float("inf"), i] for i in range(n)]
    P = [None for _ in range(n)]
    dist[src][0] = 0
    Q = []
    for i in range(n):
        heapq.heappush(Q, dist[i])
    while Q:
        u = heapq.heappop(Q)

        for v in G[u[1]]:
            if v[0] != P[u[1]]:
                if dist[v[0]][0] > dist[u[1]][0] + v[1]:
                    dist[v[0]][0] = dist[u[1]][0] + v[1]
                    P[v[0]] = u[1]

    for i in range(n):
        if i != src:
            print("Edge: ", P[i], i)
    return


G = [[[1,2],[2,50]],
     [[0,2],[5,1],[3,5],[4,10]],
     [[0,50],[4,5],[3,40]],
     [[2,40],[4,4],[5,2],[1,5]],
     [[1,10],[3,4],[2,5]],
     [[3,2],[1,1]]]

prim(G, 0)