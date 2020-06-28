class HashElement():
    def __init__(self):
        self.value = None
        self.key = None
        self.status = 0 # 0 - free, 1 - taken, 2 - free but keep looking

class Hashtable():
    def __init__(self, N):
        self.table = [HashElement() for _ in range(N)]
        self.size = N
        self.taken = 0

    def hashing(self, key):
        return key % self.size

    def insert(self, key, val):
        if self.taken == self.size:
            return
        idx = self.hashing(key)
        step = 1
        while self.table[idx].status == 1:
            idx += step
            idx %= self.size
            step *= 2
        self.table[idx].status = 1
        self.table[idx].value = val
        self.table[idx].key = key
        self.taken += 1

    def remove(self, key):
        idx = self.hashing(key)

        step = 1
        while self.table[idx].status != 0:
            if self.table[idx].status == 0 or self.taken == 0:
                print("Not exists!")
                return
            if self.table[idx].status == 1 and self.table[idx].key == key:
                self.table[idx].status = 2
                self.table[idx].value = None
                self.table[idx].key = None
                self.taken -= 1
            idx += step
            idx %= self.size
            step *= 2
        return


    def find(self, key):
        idx = self.hashing(key)


        step = 1
        while self.table[idx].status != 0:
            if self.table[idx].status == 1 and self.table[idx].key == key:
                print("Value: ", self.table[idx].value)
                return
            idx += step
            idx %= self.size
            step *= 2

        if self.table[idx].status == 0 or self.taken == 0:
            print("Not exists!")
            return

    def print(self):
        for i in range(self.size):
            print("val:", self.table[i].value, " key: ", self.table[i].key, " sta: ", self.table[i].status)

H = Hashtable(10)
H.insert(69, "Twoja stara")
H.insert(99, "To kopara")
H.insert(1, "Aj")
H.insert(222, "Caramba")
H.insert(10, "Fck")
H.find(222)
H.find(99)
H.remove(222)
H.find(222)
