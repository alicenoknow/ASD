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
    d = [[float("inf"), i] for i in range(n)]
    d[s][0] = 0
    for u in range(n):
        for v in G[u]:
                if d[v[0]][0] > d[u][0] + v[1]:
                    d[v[0]][0] = d[u][0] + v[1]
                    P[v[0]].append(u)
    for u in range(n):
        for v in G[u]:
            if d[v[0]][0] > d[u][0] + v[1]:
                print("negative cycle")
                return
    for i in range(0, len(G)):
        P[i].append(i)
        print(d[i][0], P[i])

G = [ [[1,20],[3,5],[4,0]],
     [[0,1], [2,5]],
     [[1,4],[3,5],[4,1]],
     [[1,3],[2,5],[4,10]],
     [[0,2],[2,4]]]
path = [[] for _ in range(len(G))]
bellman_ford(G, 0, path)