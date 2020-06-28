'''
Algorytm Jarvisa:
znajdz najbaedziej dolny - dodaj do otoczki
znajdz najmniej odchylony katowo - dodaj do otoczki i szukaj dla niego nastepnego takiego punktu
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


def otoczka_wypukla(P): # convex hull
    if len(P) < 3:
        return None
    O = []
    lowest = find_lowest(P)
    low = lowest

    while True:
        O.append(low)
        closest = (low + 1) % len(P)
        for i in range(len(P)):
            if clock_pos(P[i], P[low], P[closest]) == 2:
                closest = i
        low = closest
        if closest == lowest:
            break
    return O



P = []
P.append(Point(1,2))
P.append(Point(9,1))
P.append(Point(1,4))
P.append(Point(0,2))
P.append(Point(7,8))
P.append(Point(2,5))
P.append(Point(3,5))
idx = otoczka_wypukla(P)
for i in range(len(idx)):
   print(P[idx[i]].x, P[idx[i]].y)
