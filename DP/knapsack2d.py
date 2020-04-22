def knapsack2d( V, max_w, max_h ):       # max_w - maximum weight, max_h - maximum height, n - amount of items
    n = len(V)
    # F[i][w][h] - maximum profit of items from 0 to i that  total weight is <= w and  total height <= h
    F = [[[0 for _ in range(max_h+1)] for _ in range(max_w+1)] for _ in range(n)]   # initialise with 0
    for w in range(V[0][1], max_w + 1):                 # initialise with profit of first item
        for h in range(V[0][2], max_h + 1):
                   F[0][w][h] = V[0][0]

    for i in range(1, n):
        for w in range(1, max_w + 1):
            for h in range(1, max_h + 1):
                F[i][w][h] = F[i - 1][w][h]
                if w >= V[i][1] and h >= V[i][2]:       # if we can take an item, we check if it is profitable
                     F[i][w][h] = max(F[i][w][h], F[i - 1][w - V[i][1]][h - V[i][2]] + V[i][0])
    return F[n - 1][max_w][max_h]


P = [(5,10,3), (7,8,12), (2,7,3)]
print( knapsack2d( P, 16, 15 ) )    # wypisze 9