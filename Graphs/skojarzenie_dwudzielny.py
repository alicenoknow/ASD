# policz maksymalny przepływ z s do t
# c[i][j] to przepustowość krawędzi z i do j
# jeśli c[i][j] > 0 to c[j][i] = 0

def max_flow( c, s, t ):
    n = len(c)
    # F - F[i][j] opisuje obecny przeplyw z i do j
    F = [[0 for _ in range(n)] for _ in range(n)]
    # maxflow - maksymalny przeplyw
    maxflow = 0
    while True:
        # flow - przeplyw osiagniety na sciezce path
        flow, path = BFS_flow(c, F, s, t)
        # jezeli nie znaleziono zadnej dostepnej scizeki - zakoncz
        if path is None:
            break
        # jesli znaleziono sciezke, zwieksz maxflow o przeplyw na danej sciezce
        maxflow += flow
        # aktualizacja sieci przeplywu, dodajemy przeplyw tam gdzie nstapil, odejmujemy w przeciwnym kierunku
        to = t
        while to != s:
            fro = path[to]
            F[fro][to] += flow
            F[to][fro] -= flow
            to = fro

    return maxflow


def BFS_flow(c, F, s, t):
    # n - liczba wierzcholkow
    n = len(c)
    # Q - kolejka
    Q = []
    # tablica parent - z niej bede odtwarzac znaleziona scieke
    parent = [-1 for _ in range(n)]
    # przeplyw na aktualnej sciezce
    Flow = [float("inf") for _ in range(n)]
    Q.append(s)
    while Q:
        # u - aktualny wierzcholek
        u = Q.pop()
        # odwiedzamy wszystkie jego dzieci
        for v in range(n):
            # sprawdzam czy jest jeszcze przepustowosc i czy wierzcholek byl odwiedzony
            if c[u][v] - F[u][v] > 0 and parent[v] == -1:
                parent[v] = u
                # aktualizujemy obecny przeplyw do v, biorac minimum z tego wplynelo do poprzednika i z tego co
                # moze pomiescic krawedz miedzy u i v
                Flow[v] = min(Flow[u], c[u][v] - F[u][v])
                # jesli v to nie ujscie, dodajemy wierzcholek do kolejki, zeby potem odwiedzic jego dzieci
                if v == t:
                    return Flow[t], parent
                Q.append(v)
    # jesli w petli nie zostal spelniony warunek wyjscia v == t, oznacza to ze nie znaleziono sciezki to t, zwroc None
    return 0, None


def convert(data):
    N = len(data) + len(data[0]) + 2
    graph = [[0 for i in range(N)] for _ in range(N)]
    for i in range(1, len(data)+1):
        graph[0][i] = 1
        graph[N - i - 1][N-1] = 1
    for i in range(1, len(data)+1):
        for j in range(len(data)+1, N-1):
            graph[i][j] = data[i-1][j - len(data) - 1]
    for i in range(N):
        print(graph[i])
    return graph


def matching(G):
    return max_flow(convert(G), 0, 13)



# graf bez zrodla i ujscia - przyklad: pracownicy wybieraja potencjana prace 1 jesli chca 0 jesli nie
# tworzymy graf i skojarzenie pokazuje maksymalna liczbe osob ktore moga dostac prace ktora chca
applicants = [[0, 1, 1, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [1, 0, 0, 1, 0, 0],
          [0, 0, 1, 0, 0, 0],
          [0, 0, 1, 1, 0, 0],
          [0, 0, 0, 0, 0, 1]]

print(matching(applicants))