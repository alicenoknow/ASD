def surface(P):
    prev = P[0]
    S = 0
    for i in range(1, len(P)):
        if P[i][0] < prev[0]:
            S += (prev[1] + P[i][1]) * (prev[0] - P[i][0]) / 2
        else:
            S -= (prev[1] + P[i][1]) * (P[i][0] - prev[0]) / 2
        prev = P[i]
        print(S)
    if P[0][0] < prev[0]:
        S += (prev[1] + P[0][1]) * (prev[0] - P[0][0]) / 2
    else:
        S -= (prev[1] + P[0][1]) * (P[0][0] - prev[0]) / 2

    return S


P = [[1,1],[2,2],[6,1],[10,2], [7,5], [3,5], [4,6], [1.5, 6]]
print(surface(P))