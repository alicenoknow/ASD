'''
wejście: graf ważony skierowany o nieujemnych wagach
złożoność dla list adjacencji: O(E * log(V))
złożoność dla macierzy adjacencji: O(E * log(V))
'''

import heapq as hp


def dijkstra(G, s, P):
    d = [[float("inf"), i] for i in range(len(G))]
    d[s][0] = 0
    Q = []
    for i in range(len(G)):
        hp.heappush(Q, d[i])
    while len(Q):
        u = hp.heappop(Q)
        for v in range(len(G[u[1]])):
            if G[u[1]][v] is not None:
                if d[v][0] > u[0] + G[u[1]][v]:
                    d[v][0] = u[0] + G[u[1]][v]
                    P[v].append(u[1])
    for i in range(0, len(G)):
        P[i].append(i)
        print(d[i][0], P[i])




G = [[None, 32, 72, 4, None],
     [None, None, 4, None, None],
     [2, 42, None, 52, 532],
     [2, 1, 4, None, 1],
     [1, 5, 1, 4, None]]
path = [[] for _ in range(len(G))]
dijkstra(G, 1, path)