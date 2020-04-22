from sys import maxsize


def count_shortest_paths(G, s, t):
    n = len(G)                          # liczba wierzcholkow
    visit = [False] * n                 # tablica przechowujaca informacje czy wierzcholek byj juz odwiedzony
    d = [maxsize] * n                   # odleglosc od wierzcholka poczatkowego s
    count = [0] * n                     # tablica przechowujaca liczbe tras do i-tego wierzcholka
    d[s] = 0
    count[s] = 1
    Q = [s]                             # inicjowanie kolejki
    visit[s] = True

    while Q:
        v = Q.pop()                     # sciagam wierzcholek z kolejki
        if v == t:                      # jezeli jest rowny wierzolkowi koncowemu to nie trzeba go przetwarzac
            v = Q.pop()                 # bo nie interesuja nas trasy przechodzace przez niego
        for i in (i for i in range(0, n) if G[v][i] is True):       # po kolei zczytuje sasiadow v
            if not visit[i]:                                        # jesi nie byl odwiedzony, zostaje dodany do kolejki
                Q.append(i)
                visit[i] = True
            if d[i] > d[v] + 1:                 # jezeli dotychczasowa trasa do wierzcholka i byla dluzsza niz
                d[i] = d[v] + 1                 # ta przechodzaca przez v to zapisujemy dla niego nowa najkrotsza trase
                count[i] = count[v]             # narazie takich tras jest tyle ile najkrotszych tras do v
            elif d[i] == d[v] + 1:              # jesli trasa do i przez v jest rowna obecnie najkrotszej trasie do i
                count[i] += count[v]            # to zwiekszamy licznik najkrotszych tras dla i
    return count[t]


G = [[False, True, True, False],
[False, False, True, True ],
[False, False, False, True ],
[False, False, False, False]]
print( count_shortest_paths( G, 0, 3 ) )    # wypisze 2