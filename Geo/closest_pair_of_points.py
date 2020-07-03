from math import sqrt
'''
O (n log n) ale jeszcze bez tej 7, ogarnac Cormena
'''

class Point:
    def __init__(self, x=None, y=None, i=None):
        self.x = x
        self.y = y
        self.pos2 = i


def dist(p1, p2):
    return sqrt((p2.x-p1.x)*(p2.x-p1.x) + (p2.y-p1.y)*(p2.y-p1.y))


def partition(arr, arr2, l, r, key):
    i = l - 1
    pivot = arr[r]
    for j in range(l, r):
        if key and arr[j].y <= pivot.y:
            i += 1
            arr2[arr[i].pos2].pos2 = j
            arr2[arr[j].pos2].pos2 = i
            arr[i], arr[j] = arr[j], arr[i]
        elif not key and arr[j].x <= pivot.x:
            i += 1
            arr2[arr[i].pos2].pos2 = j
            arr2[arr[j].pos2].pos2 = i
            arr[i], arr[j] = arr[j], arr[i]
    arr2[arr[i + 1].pos2].pos2 = r
    arr2[arr[r].pos2].pos2 = i + 1
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


def quicksort(arr, arr2, l, r, key):    # 0 - x, 1 - y
    if l < r:
        piv = partition(arr, arr2, l, r, key)
        quicksort(arr, arr2, l, piv - 1, key)
        quicksort(arr, arr2, piv + 1, r, key)


def brute(P, n):
    min_dist = float("inf")
    for i in range(n):
        for j in range(i+1, n):
            if dist(P[i], P[j]) < min_dist:
                min_dist = dist(P[i], P[j])
    return min_dist


def strip_closest(S, size, d):
    min_d = d
    for i in range(size):
        for j in range(i+1, size):
            if j < size and (S[j].y - S[i].y) < min_d:
                if dist(S[i], S[j]) < min_d:
                    min_d = dist(S[i], S[j])
    return min_d


def closest_util(Px, Py, N):
    if N < 4:
        return brute(Px, N)
    mid = N//2
    mid_point = Px[mid]
    cnt = 0
    L = []
    R = []
    for i in range(N):
        if Py[i].x <= mid_point.x and cnt < mid:
            L.append(Py[i])
            cnt += 1
        else:
            R.append(Py[i])
    dL = closest_util(Px, L, mid)
    dR = closest_util(Px, R, N - mid)
    d = min(dR, dL)
    S = []
    j = 0
    for i in range(N):
        if abs(Py[i].x - mid_point.x) < d:
            S.append(Py[i])
            j += 1
    return strip_closest(S, j, d)


def find_closest(P):
    N = len(P)
    Px = [Point(P[i].x, P[i].y, i) for i in range(N)]
    Py = [Point(P[i].x, P[i].y, i) for i in range(N)]
    quicksort(Px, Py, 0, N - 1, 0)
    quicksort(Py, Px, 0, N - 1, 1)
    return closest_util(Px, Py, N)



P = []
P.append(Point(3,5))
P.append(Point(32,10))
P.append(Point(73,53))
P.append(Point(34,53))
P.append(Point(8,12))
print(find_closest(P))
print(dist(Point(3,5), Point(8,12)))