'''
Algorytm Grahama
O( n log n)
otoczka wypukła
znajdz najbardziej dony punkt lowest
posortuj punkty po wspolrzednej katowej wzgledem lowest
'''

class Point:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y


def clock_pos(p1, low, p2):
    pos = (low.x - p1.x) * (p2.y - low.y) - (low.y - p1.y) * (p2.x - low.x)
    # colinear
    if pos == 0:
        return 0
    # clockwise
    elif pos > 0:
        return 1
    #counter-clockwise
    return 2


def find_lowest(P):
    lowest = 0
    for i in range(1, len(P)):
        if P[i].y < P[lowest].y:
            lowest = i
        elif P[i].y == P[lowest].y and P[i].x < P[lowest].x:
            lowest = i
    return lowest


def partition(arr, l, r, lowest):
    i = l - 1
    pivot = arr[r]
    for j in range(l, r):
        if clock_pos(pivot, lowest, arr[j]) < 2:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


def quicksort(arr, l, r, lowest):
    if l < r:
        piv = partition(arr, l, r, lowest)
        quicksort(arr, l, piv - 1, lowest)
        quicksort(arr, piv + 1, r, lowest)


def otoczka(P):
    if len(P) < 3:
        return None

    lowest = find_lowest(P)
    quicksort(P, 0, len(P)-1, P[lowest])
    O = []
    for point in P:
        while len(O) > 1 and clock_pos(O[-2], O[-1], point) == 2:
            O.pop()
        O.append(point)
    for point in O:
        print(point.x, point.y)


P = []
P.append(Point(1,2))
P.append(Point(9,1))
P.append(Point(1,4))
P.append(Point(0,2))
P.append(Point(7,8))
P.append(Point(2,5))
P.append(Point(3,5))
otoczka(P)