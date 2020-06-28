# O(V + E)
def BFS( G, s ):
    v = len(G)          # liczb wierzcholkow
    Q = []              # kolejka
    res = [[None, 0] for _ in range(v)]
    Q.append(s)
    while Q != []:
        u = Q.pop()                     # u - aktualny wierzcholek
        for i in range(0, v):           # odwiedzamy wszystkie jego dzieci
            if G[u][i] == 1:
                if res[i][0] == None:           # jesli nie bylismy w tym wierzcholku - nie ma uzupelnionego pola parent
                    res[i][0] = u               # to parent = u
                    res[i][1] = res[u][1] + 1   # odleglosc od s o jeden wieksza niz jego parent
                    Q.append(i)                 # wrzucamy go do kolejki zeby potem odwiedzic jego dzieci
    return res


# elementarny test, powinien wypisać
# [(None,0), (0,1), (0,1), (2,2)]
# lub
# [(None,0), (0,1), (0,1), (1,2)]
G = [[0,1,1,0],[0,0,0,1],[0,1,0,1], [0,0,0,0]]
print( BFS(G,0) )
