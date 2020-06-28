class HashElement():
    def __init__(self):
        self.value = None
        self.key = None
        self.status = 0 # 0 - free, 1 - taken, 2 - free but keep looking

def hashing(key, size):
    return key % size

class Hashtable():
    def __init__(self, N):
        self.table = [HashElement() for _ in range(N)]
        self.size = N
        self.taken = 0

    def insert(self, key, val):
        if self.taken == self.size:
            return
        idx = hashing(key, self.size)
        while self.table[idx].status == 1:
            idx += 1
            idx %= self.size
        self.table[idx].status = 1
        self.table[idx].value = val
        self.table[idx].key = key
        self.taken += 1

    def remove(self, key):
        idx = hashing(key, self.size)
        while self.table[idx].status != 0:
            if self.table[idx].status == 0 or self.taken == 0:
                print("Not exists!")
                return
            if self.table[idx].status == 1 and self.table[idx].key == key:
                self.table[idx].status = 2
                self.table[idx].value = None
                self.table[idx].key = None
                self.taken -= 1
            idx += 1
            idx %= self.size
        return


    def print(self):
        for i in range(self.size):
            print("val:", self.table[i].value, " key: ", self.table[i].key, " sta: ", self.table[i].status)


def correct(H, N):
    P = [None for _ in range(N)]
    for i in range(N):
        for j in range(0, i+1):
            if H[j].status == 0:
                P[i] = j
    print(P)
    for i in range(N):
        if H[i].status == 1:
            idx = hashing(H[i].key, N)
            if i != idx:
                if idx > i:
                    if P[i] is not None:
                        return False
                    if P[N-1] is not None and P[N-1] >= idx:
                        return False
                else:
                    if P[i] is not None and P[i] >= idx:
                        return False
    return True



H = Hashtable(10)
a = HashElement()
b = HashElement()
a.key = 3
a.val = 1
a.status = 1
b.key = 8
b.val = 8
b.status = 1
H.table[5] = a
H.table[6] = b
print(correct(H.table, H.size))
H.print()