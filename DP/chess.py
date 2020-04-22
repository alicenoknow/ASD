def chess(A,n):
    if n == 0: return -1
    DP = [None] * n
    for i in range(n):
        DP[i] = [0]*n
    for j in range(n):
        if i == 0:
            DP[i][j] = DP[i][j-1] + A[i][j]
        elif j == 0:
            DP[i][j] = DP[i-1][j] + A[i][j]
        else:
            DP[i][j] = A[i][j] + min(DP[i][j-1], DP[i-1][j])