'''
problem: znaleźć najkrótsze ścieżki z wierzchołka źródłowego do wszystkich pozostałych wierzchołków
wejście: graf ważony skierowany o dowolnych wagach
idea: k-ta relaksacja znajduje najkrótsze ścieżki o długości do k włącznie (dowód - Cormen);
najdłuższa możliwa ścieżka niebędąca cyklem (w sensie liczby wierzchołków) ma długość V - 1,
więc tyle razy trzeba zrelaksować wszystkie krawędzie; w ten sposób każdy wierzchołek w każdej z V - 1 iteracji
 “dowiaduje się” o najkrótszych ścieżkach długości o 1 większej niż poprzednio znane
wykrywa negatywne cykle - jeżeli w grafie jest cykl o sumie ujemnej, to te relaksacje to ujawnią
i na koniec trzeba sprawdzić, czy taki cykl jest; jeżeli tak, to zwracamy informację o tym, a nie najkrótsze ścieżki;
w Cormenie zwracany jest False
złożoność: O(V * E)
'''

def bellman_ford(G, s, P):
    n = len(G)
    d = [float("inf") for _ in range(n)]
    d[s] = 0
    for u in range(n):
        for v in range(n):
            if G[u][v] is not None:
                if d[v] > d[u] + G[u][v]:
                    d[v] = d[u] + G[u][v]
                    P[v].append(u)
    for u in range(n):
        for v in range(n):
            if G[u][v] is not None and d[v] > d[u] + G[u][v]:
                print("negative cycle")
                return
    for i in range(0, len(G)):
        P[i].append(i)
        print(d[i], P[i])

G = [[None, 32, 72, 4, None],
     [None, None, 4, None, None],
     [2, 3, None, 52, 532],
     [2, 1, 4, None, 1],
     [1, 5, 1, 4, None]]
path = [[] for _ in range(len(G))]
bellman_ford(G, 1, path)