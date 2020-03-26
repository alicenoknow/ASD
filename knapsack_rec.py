def knapsack_rec(W, P, maxW):
    n = len(W)                      # maxW - maksymalna waga, n - ilosc przedmiotow
    memo = n * [None]               # memo[i][w] - maksymalny profit z przedmiotow do i-tego i wadze <= w
    for i in range(n):
        memo[i] = [-1] * (maxW + 1)              # inicjuje memo -1
    a = _knapsack_rec(W, P, memo, maxW, n)
    result = memo[n-1][maxW]
    w = maxW
########################################### WYPISYWANIE ###############################################################
    for i in range(n-1, 0, -1):             # uzywajac tablicy memo mozemy odtworzyc ktore przedmioty zostaly uzyte
        if(result != memo[i-1][w]):         # jesli profit miedzy i a i-1 przedmiotem sie nie zmienia to zanczy ze
            print("Item index: ", i)        # go nie uzylismy, jesli sie zmienia to wypisujemy
            result -= P[i]
            w -= W[i]
    return a


def _knapsack_rec(W, P, memo, maxW, n):
    if n == 0 or maxW == 0:                     # warunek brzegowy rekurencji - nie ma juz przedmiotow lub nie mamy juz miejsca
        return 0
    if memo[n-1][maxW] != -1:                    # jesli juz policzylismy wartosc wczesniej zwroc
        return memo[n-1][maxW]
    if maxW < W[n-1]:                               # sprawdzamy czy mozemy wziac n-ty przedmiot
        return _knapsack_rec(W, P, memo, maxW, n-1)
    else:                                               # jesli tak to sprawdzamy czy jest to oplacalne
        memo[n-1][maxW] = max(_knapsack_rec(W, P, memo, maxW, n-1), P[n-1] + _knapsack_rec(W, P, memo, maxW - W[n-1], n-1))
    return memo[n-1][maxW]
