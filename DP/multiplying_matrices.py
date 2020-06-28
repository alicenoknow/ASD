def multiplying_matrices(rows, cols):
    n = len(rows)
    dp = [[float("inf") for _ in range(n)] for _ in range(n)]
    P = [[float("inf") for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0
    for L in range(2, n+1):
        for i in range(0, n-L+1):
            j = i + L-1
            for k in range(i, j):
                if dp[i][j] > dp[i][k] + dp[k+1][j] + rows[i]*cols[k]*cols[j]:
                    dp[i][j] = dp[i][k] + dp[k+1][j] + rows[i]*cols[k]*cols[j]
                    P[i][j] = k
    N = 1
    print_brackets(0, n-1, N, P)


def print_brackets(i, j, N, P):
    if i == j:
        print(N, end="")
        N += 1
        return N
    print("(", end="")
    N = print_brackets(i, P[i][j], N, P)
    N = print_brackets(P[i][j]+1,j, N, P)
    print(")", end="")
    return N





rows = [5,4,6,2]
cols = [4,6,2,7]
multiplying_matrices(rows, cols)