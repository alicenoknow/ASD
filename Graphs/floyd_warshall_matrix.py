'''
Algorytm Floyda Warshalla działa dla każdego grafu, zawsze w złożoności O(V^3),
co dla grafów gęstych jest lepsze niż Dixtra każdy z każdym. Jego złożoność pamięciowa
wynosi zawsze O(V^2). Algorytm nie może zostać wykorzystany do obliczenia najkrótszych ścieżek
między wierzchołkami z jakiegoś podzbioru wierzchołków.
'''

def print_path(P,s,t):
    v = [t]
    print("Path from", s, "to", t, ": ")
    while s != t:
        v.append(P[s][t])
        t = P[s][t]
    print(list(reversed(v)), "\n")


def print_dist(D):
    for row in D:
        for val in row:
            print(val, end = " ")
        print()


def floyd_warshall(G, D, P):
    n = len(G)
    for u in range(n):
        for v in range(n):
            for w in range(n):
                if D[v][w] > D[v][u] + D[u][w]:
                    D[v][w] = D[v][u] + D[u][w]
                    P[v][w] = u
    print_path(P,2,4)
    print_dist(D)


G = [[0, 32, 72, 4,float("inf")],
     [float("inf"), 0, 4, 12, float("inf")],
     [2, 2, 0, 52, 532],
     [23, 16, 4, 0, 16],
     [154, 5, 16, 4, 0]]

D = [[G[u][v] for v in range(len(G))] for u in range(len(G))]
P = [[None for _ in range(len(G))] for _ in range(len(G))]
for i in range(len(G)):
    for j in range(len(G)):
        if i == j:  P[i][j] = None
        elif G[i][j] != float("inf"):
            P[i][j] = i

floyd_warshall(G,D,P)
