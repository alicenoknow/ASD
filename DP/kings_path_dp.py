def kings_path(A):
    n = len(A)
    dp = [[float("inf") for _ in range(n)] for _ in range(n)]
    dp[0][0] = A[0][0]

    for i in range(0,n):
        for j in range(0,n):
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j] + A[i][j])
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j-1] + A[i][j])

    for i in range(n):
        print(dp[i])


A = [[1, 2, 3, 4, 51],
     [6, 10, 4, -9, 2],
     [0, 12, 10, 10, 10],
     [12, 13, 12, -11, 3],
     [1, 2, 0, 10, 10]]

kings_path(A)