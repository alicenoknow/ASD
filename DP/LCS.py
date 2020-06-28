# recursive
def _LCS(s1, s2, i1, i2, memo):
    if i1 == len(s1) or i2 == len(s2):
        return 0
    if memo[i1][i2] is not None:
        return memo[i1][i2]
    if s1[i1] == s2[i2]:
        result = 1 + _LCS(s1, s2, i1 + 1, i2 + 1, memo)
    else:
        result = max(
            _LCS(s1, s2, i1 + 1, i2, memo),
            _LCS(s1, s2, i1, i2 + 1, memo))
        memo[i1][i2] = result
    return result


def LCS(s1, s2):
    memo = [[None for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    return _LCS(s1, s2, 0, 0, memo)

# iteration
def LCS_iter(s1, s2):
    dp = [[None for _ in range(len(s2))] for _ in range(len(s1))]
    n = len(s1)-1
    m = len(s2)-1
    for i in range(n+1):
        dp[i][m] = 0
    for i in range(m+1):
        dp[n][i] = 0
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if s1[i] == s2[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])
    return dp[0][0], dp


def printLCS(s1,s2):
    pass

s1 = "aalaagaaaraa"
s2 = "ligrbkjb"
print(LCS(s1,s2))
print(printLCS(s1,s2))