from math import floor,sqrt


class Cyclist:
    def __init__(self, p=None, c=None, n=None):
        self.prev = p
        self.curr = c
        self.next = n

class Hashtable:
    def __init__(self, N):
        self.table = [[] for _ in range(N)]
        self.size = N

    def hashing(self, key):
        a = (sqrt(5) - 1) / 2
        return floor(self.size * ((float(key) * a) % 1))

    def insertCN(self, val):
        idx = self.hashing(val.curr)
        for i in range(len(self.table[idx])):
            if self.table[idx][i].curr == val.curr:
                self.table[idx][i].next = val.next
                return
        self.table[idx].append(val)

    def insertP(self, val):
        idx = self.hashing(val.curr)
        for i in range(len(self.table[idx])):
            if self.table[idx][i].curr == val.curr:
                self.table[idx][i].prev = val.prev
                return
            self.table[idx].append(val)

    def find(self, key):
        idx = self.hashing(key)
        for i in range(len(self.table[idx])):
            if self.table[idx][i].curr == key:
                return self.table[idx][i].next

    def print(self):
        for i in range(self.size):
            for j in range(len(self.table[i])):
                print("p: ", self.table[i][j].prev ," c: ", self.table[i][j].curr," n: ", self.table[i][j].next)

def peleton(C):
    N = len(C)
    H = Hashtable(N)
    for i in range(N):
        c = Cyclist(-1, C[i][0], C[i][1])
        H.insertCN(c)
        if C[i][1] != -1:
            c = Cyclist(C[i][0], C[i][1], -1)
            H.insertP(c)
    M = 1
    size = 1
    for i in range(N):
        if len(H.table[i]) > 0:
            for j in range(len(H.table[i])):
                if H.table[i][j].prev == -1 and H.table[i][j].next != -1:
                    n = H.table[i][j].next
                    while True:
                        size += 1
                        n = H.find(n)
                        if n == -1:
                            break
                    if size > M:
                        M = size
                        size = 1
    return M


C = [[10, -1],[8, -1],[7, 8],[3, 2],[2, -1],[4, 1],[5, -1],[1, 5]]

print(peleton(C))