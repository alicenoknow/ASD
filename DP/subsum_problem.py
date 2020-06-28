def subsum(arr, sum):
    n = len(arr)
    if sum == 0:
        return True
    if n == 0:
        return False

    dp = [[False for _ in range(sum+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = True

    for i in range(1, n+1):
        for j in range(1, sum+1):
            if j < arr[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = (dp[i-1][j] or dp[i-1][j-arr[i-1]])

    for i in range(n+1):
        print(dp[i])
        print()


arr = [6, 3, 7, 6, 1, 4, 3, 10, 8]
sum = 18
subsum(arr,sum)