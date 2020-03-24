def LIS(tab):  # Longest Increasing Subsequence O(n^2)
    n = len(tab)
    sub = n * [1]
    val = [-1] * n
    for i in range(1, n):
        for j in range(i):
            if tab[j] < tab[i] and sub[i] < sub[j] + 1:
                sub[i] = sub[j] + 1
                val[i] = j
    for i in range(n):
        if(sub[i] == max(sub)):
            idx = i
    return max(sub), idx, val


def printLIS(tab, val, i):
    if (val[i]) >= 0:
        printLIS(tab, val, val[i])
    print(tab[i])


def LIS_better(tab):    # O(n*log(n))
    pass


tab = [2, 5, 3, 7, 8, 1, 5, 1, 11, 23, 9]
l, idx, val = LIS(tab)
printLIS(tab, val, idx)