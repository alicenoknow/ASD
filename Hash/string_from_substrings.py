'''
S - tablica substrings, t - napis
znajdz minimalna ilosc substringow aby stworzyc napis t
'''

min_s = float("inf")


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
    global min_s
    if start == len(t):
        min_s = min(cnt, min_s)

    for length in range(1, len(t) - start + 1):
        subStr = t[start: start + length]

        if H.find(subStr):
            util(t, cnt + 1, start + length, H)


def min_substrings(S, t):
    N = len(S)
    H = Hashtable(N)
    for i in range(N):
        H.insert(S[i], S[i])
    util(t, 0, 0, H)
    print(min_s)


S = ["1", "22", "13", "348", "3", "192", "2", "4"]
t = "1234"
min_substrings(S, t)