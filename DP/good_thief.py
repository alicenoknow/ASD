def good_thief(A, n):
    # 0 - bez, 1 - z
    dp = [[0, 0] for _ in range(n)]
    items = []
    dp[0][1] = A[0]
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1])
        dp[i][1] = dp[i-1][0] + A[i]
    profit = max(dp[n-1][0], dp[n-1][1])
    print_items(A, dp, n-1, items, profit)


def print_items(A, dp, idx, items, profit):
    if idx < 0:
        print(items)
        return
    if profit == dp[idx][0]:
        print_items(A, dp, idx - 1, items, profit)
    else:
        items.append(idx)
        profit -= A[idx]
        print_items(A, dp, idx - 1, items, profit)



A = [1,3,3,22]
good_thief(A, len(A))