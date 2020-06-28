def knapsack(W, P, maxW):      # W[i] - weight of i-th item, P[i] - profit of i-th item,
    n = len(W)                  # maxW - max possible weight we can handle, n - amount of items
    to_print = n *[None]        # array  which will be used to print items in the end
    F = n * [None]              # F[i][w] - maximum profit of items from 0 to i that total weight is <= w
    for i in range(n):
        F[i] = [0] * (maxW + 1)         # initialize F with 0, F[i][0] = 0
        to_print = [0] * (maxW + 1)
    for w in range(W[0], maxW + 1):     # if weight of 0 item is <= maxW then F[0][i] = P[0]
        F[0][w] = P[0]
    for i in range(1, n):
        for w in range(1, maxW + 1):
            F[i][w] = F[i-1][w]
            if w >= W[i]:                                        # if we can still take our item
                F[i][w] = max(F[i][w], F[i-1][w-W[i]] + P[i])    # we check whether it is profitable
    result = F[n-1][maxW]
    w = maxW
    for i in range(n-1, -1, -1):
        if result != F[i][w]:
            print(W[i])
            result -= P[i]
            w -= w[i]
    return F[n-1][maxW]

W = [1,2,5,3,8,5,7,9,2]
P = [2,7,5,4,6,9,2,1,4]
maxW = 14
res = knapsack(W,P,maxW)
print(res)

# how to print which items we take