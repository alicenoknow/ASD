def coins_change(coins, sum):
        res = [[0 for _ in range(sum + 1)] for _ in range(len(coins) + 1)]
        m = [[0 for _ in range(sum + 1)] for _ in range(len(coins) + 1)]
        for i in range(1, sum + 1):
            m[0][i] = float('inf')
        for c in range(1, len(coins) + 1):
            for r in range(1, sum + 1):
                if coins[c - 1] == r:
                    m[c][r] = 1
                    res[c][r] = coins[c-1]
                elif coins[c - 1] > r:
                    m[c][r] = m[c - 1][r]
                else:
                    if 1 + m[c][r - coins[c - 1]] < m[c - 1][r]:
                        m[c][r] = 1 + m[c][r - coins[c - 1]]
                        res[c][r] = coins[c-1]
                    else:
                        m[c][r] = m[c - 1][r]
                        res[c][r] = coins[c - 2]

        i = len(coins) 
        j = sum
        while j >= 1:
            print(res[i][j], end=" ")
            j -= res[i][j]
            if res[i][j] == 0:
                i -= 1
            '''
        for i in range(len(coins) +1):
            print(res[i])
            '''
        return m[-1][-1]






sum = 16
Coins = [1, 5, 8]
coins_change(Coins, sum)