def cut_rod(P, L, l):
    n = len(P)
    printing = [0 for _ in range(l+1)]
    dp = [0 for _ in range(l+1)]
    dp[0] = 0
    for i in range(1, l+1):
        dp[i] = dp[i-1]
        for j in range(1, i+1):
            if dp[i] < dp[i-j] + P[j-1]:
                dp[i] = dp[i-j] + P[j-1]
                printing[i] = j
    #printing
    i = l
    print("Pieces: ")
    while i:
        print(printing[i], end=" ")
        i = i - printing[i]
    return dp

P = [1,4,5,8,10,1,9,2,1]
L = [1,2,3,4,5,6,7,8,9]
l = 9

print("\nProfit:", cut_rod(P, L, l)[l])
