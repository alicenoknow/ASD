from math import floor,sqrt
from random import randint

class Hashtable:
    def __init__(self, N):
        self.size = N

    def hash_string(self, key):
        p = 2137
        h = 0
        for i in range(len(key)):
            h = h*p + ord(key[i])
        return h % self.size

    def hash_simple(self, key):
        return key % self.size

    def hash_floor(self, key):
        a = (sqrt(5) - 1)/ 2
        return floor(self.size * ((key * a) % 1))

    def hash_prime_create(self):
        p = 997
        a = randint(1, p - 1)
        b = randint(0, p - 1)
        return a, b, p

    def hash_prime(self, key, a, b, p):
        return ((a*key + b) % p ) % self.size


H = Hashtable(100)
a,b,p = H.hash_prime_create()
print(H.hash_prime(79126, a, b, p))