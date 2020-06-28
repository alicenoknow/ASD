def LIS(tab):  # Longest Increasing Subsequence O(n^2)
    n = len(tab)
    sub = n * [1]       # sub[i] biggest substring from 0 to i
    val = [-1] * n
    for i in range(1, n):
        for j in range(i):
            if tab[j] < tab[i] and sub[i] < sub[j] + 1:     # if we can add i element and it is better then current val
                sub[i] = sub[j] + 1                         # we increase sub value
                val[i] = j                                  # remember element before i to print later
    for i in range(n):
        if(sub[i] == max(sub)):
            idx = i
    return max(sub), idx, val


def printLIS(tab, val, i):
    if (val[i]) >= 0:
        printLIS(tab, val, val[i])
    print(tab[i])


def find_place(arr, l, r, val):
    while l < r:
        mid = (l + r)//2
        if arr[mid] < val:
            l = mid + 1
        else:
            r = mid
    return r

def LIS_better(tab):    # O(n*log(n))
    n = len(tab)
    l = 1
    dp = [0 for _ in range(n)]
    dp[0] = tab[0]
    for i in range(1, n):
        if tab[i] < dp[0]:
            dp[0] = tab[i]
        elif tab[i] > dp[l-1]:
            dp[l] = tab[i]
            l += 1
        else:
            dp[find_place(dp, 0, l-1, tab[i])] = tab[i]
    return l



tab = [2, 5, 3, 7, 8, 1, 5, 1, 11, 23, 9]
l, idx, val = LIS(tab)
printLIS(tab, val, idx)
print(LIS_better(tab))