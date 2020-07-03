class Hashtable:
    def __init__(self, N):
        self.table = [[] for _ in range(N)]
        self.size = N

    def hashing(self, key):
        return key % self.size

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
        print("Not exists!")
        return None

    def remove(self, key):
        idx = self.hashing(key)
        for i in range(len(self.table[idx])):
            if self.table[idx][i][0] == key:
                self.table[idx].pop(i)
                return
        print("Not exists!")
        return



H = Hashtable(10)
H.insert(69, "Twoja stara")
H.insert(99, "To kopara")
H.insert(1, "Aj")
H.insert(222, "Caramba")
H.insert(10, "Fck")
print(H.find(222))
H.find(99)
H.remove(222)
H.find(222)
