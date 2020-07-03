'''
S - tablica substrings, t - napis
znajdz maksymalna szerokosc substringow aby stworzyc napis t
np. dla t = 1234
s1 = 12 s2 = 34, wtedy width = 2
s1 = 1 s2 = 234 wtedy width = 1
'''

width = 0


class Hashtable:
    def __init__(self, N):
        self.table = [[] for _ in range(N)]
        self.size = N

    def hashing(self, key):
        p = 997
        h = 0
        for i in range(len(key)):
            h = h * p + ord(key[i])
        return h % self.size

    def insert(self, key, val):
        idx = self.hashing(key)
        for i in range(len(self.table[idx])):
            if self.table[idx][i][0] == key:
                self.table[idx][i][1] = val
                return
        self.table[idx].append([key, val])

    def find(self, key):
        idx = self.hashing(key)
        for i in range(len(self.table[idx])):
            if self.table[idx][i][0] == key:
                return self.table[idx][i][1]
        return None


def util(t, cnt, start, H):
    global width
    if start == len(t):
        width = max(width, cnt)

    for length in range(1, len(t) - start + 1):
        subStr = t[start: start + length]

        if H.find(subStr):
            cnt = len(subStr)
            if cnt != len(t):
                cnt = min(cnt, len(t)-cnt)
            util(t, cnt, start + length, H)


def min_substrings(S, t):
    N = len(S)
    H = Hashtable(N)
    for i in range(N):
        H.insert(S[i], S[i])
    util(t, 0, 0, H)
    print(width)


S = ["1", "12", "13", "324", "34", "192", "234", "124"]
t = "1234"
min_substrings(S, t)