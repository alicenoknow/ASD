def LCS(A, B):
    sub = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]

    for i in range(len(A)+1):
        sub[i][0] = 0
    for i in range(len(B)+1):
        sub[0][1] = 0
    for i in range(1,len(A)+1):
        for j in range(1,len(B)+1):
            if A[i-1] == B[j-1]:
                sub[i][j] = sub[i-1][j-1] + 1
            else:
                sub[i][j] = max(sub[i-1][j], sub[i][j-1])
    for i in range(len(sub)):
        print(sub[i])

    i = len(A)
    j = len(B)
    while i > 0 and j > 0:
        j -= 1
        if sub[i][j] > sub[i][j-1]:
            print(B[j - 1], end=" ")
            i -= 1

A = "Twoja"
B = "aTrojaa"
LCS(A,B)