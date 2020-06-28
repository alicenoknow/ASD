def sort_second(val):       #[start][end][profit]
    return val[1]

def pick_activity(A):
    A.sort(key=sort_second)
    dp = [0 for _ in range(len(A))]
    for i in range(0, len(A)):
        for j in range(0, i):
            if A[i][0] >= A[j][1]:
                dp[i] = max(dp[i], dp[j] + A[i][2])
    print(dp)


A = [[1,2,5],
     [2,5,3],
     [3,6,6],
     [4,5,2],
     [4,6,6],
     [6,8,7]]
pick_activity(A)
