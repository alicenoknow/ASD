'''
W lesie znajduje się n drzew stojących w jednej linii. Każde drzewo posiada określoną wartość, która
należy traktować jako zysk po jego wycięciu. Nie możemy wyciąć więcej niż dwóch drzew pod rząd.
Proszę zaimplementować funkcję pozwalającą określić które drzewa należy wyciąć, aby sumaryczny zysk
był jak największy.
'''

def cut_trees(Trees):
    # DP[i][0] - zysk bez wycinania i-tego drzewa
    # DP[i][1] - zysk jesli wycinamy i-te drzewo, ale i-1 nie
    # DP[i][2] - zysk jesli wycinamy i-te drzewo, ale i+1 nie
    N = len(Trees)
    DP = [[None, None, None] for _ in range(N)]
    DP[0] = [0, Trees[0], Trees[0]]
    for i in range(1, N):
        DP[i][0] = max(DP[i-1][0], DP[i-1][1], DP[i-1][2])
        DP[i][1] = DP[i-1][0] + Trees[i]
        DP[i][2] = max(DP[i-1][0] + Trees[i], DP[i-1][1] + Trees[i])
    return max(DP[N-1][0], DP[N-1][1], DP[N-1][2])

T = [2,1,3,5,6,3,7,23,3]

print(cut_trees(T))