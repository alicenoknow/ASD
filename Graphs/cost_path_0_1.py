from sys import maxsize


def path_cost( G, s, t):
    n = len(G)                   # liczba wierzchołków grafu
    cost = [0] * n                  # pomocnicza tablica kosztow
    for i in range(n):
        cost[i] = maxsize           # narazie wszystkie koszty ustawiam na max
    cost[s] = 0                     # koszt trasy ze zrodla do zrodla jest rowny 0
    Q = []                       # incjalizacja kolejki
    Q.append(s)
    while Q:
        v = Q.pop()                                 # sciagam z kolejki wierzcholek
        for i in range(len(G[v])):                  # sprawdzam jego sasiadow
            if cost[G[v][i][0]] > cost[v] + G[v][i][1]:   # jezeli aktualny koszt trasy do sasiada jest wiekszy
                cost[G[v][i][0]] = cost[v] + G[v][i][1]   # niz koszt trasy aktualnego wierzcholka + trasy miedzy nimi
                if G[v][i][1] == 0:                       # to przypisuje aktualnie sprawdzanemu wierzcholki nowy koszt
                    Q.append(G[v][i][0])                  # jesli koszt trasy miedz v a sasiadem jest rowny 0
                else:                                     # to sasiad jest umieszczany na koncu kolejki
                    Q.insert(0, G[v][i][0])                # jesli koszt jest rowny 1 to na koniec kolejki
    return cost[t]


G = [[(1,0), (2,1)],
[(3,1), (2,0)],
[(3,0)],
[]]
print( path_cost( G, 0, 3 ) ) # wypisze 0
# lista informacji o wierzchołkach do których
# jest bezpośrednia krawędź z wierzchołka i
# np. G[i] = [(7,0), (4,1), (8,1), (2,0)] oznacza, że z wierzchołka
# i są krawędzie do wierzchołków 7 (koszt 0), 4 (koszt 1),
# 8 (koszt 1) i 2 (koszt 0)
