'''
Design data structure that allows operations get_min(), get_max() and insert() in O(log N)
Idea: structure keeps two heaps - min heap and max heap with two values - [actual value, index in another heap]
'''

def left_child(i): return 2*i
def right_child(i): return 2*i + 1
def parent(i): return i//2
def heap_size(arr): return arr[0]


def max_heapify(arr, arr2, i):
    l = left_child(i)
    r = right_child(i)
    max = i
    if l <= heap_size(arr) and arr[l][0] > arr[max][0]: max = l
    if r <= heap_size(arr) and arr[r][0] > arr[max][0]: max = r
    if max != i:
        arr[max], arr[i] = arr[i], arr[max]
        arr2[arr[max][1]][1], arr2[arr[i][1]][1] = arr2[arr[i][1]][1], arr2[arr[max][1]][1]
        max_heapify(arr, arr2, max)


def build_max_heap(arr, arr2):
    for i in range(heap_size(arr)//2, 0, -1):
        max_heapify(arr,arr2, i)


def min_heapify(arr, arr2,  i):
    l = left_child(i)
    r = right_child(i)
    min = i
    if l <= heap_size(arr) and arr[l][0] < arr[min][0]: min = l
    if r <= heap_size(arr) and arr[r][0] < arr[min][0]: min = r
    if min != i:
        arr[min], arr[i] = arr[i], arr[min]
        arr2[arr[min][1]][1], arr2[arr[i][1]][1] = arr2[arr[i][1]][1], arr2[arr[min][1]][1]
        min_heapify(arr,arr2, min)


def build_min_heap(arr, arr2):
    for i in range(heap_size(arr)//2, 0, -1):
        min_heapify(arr, arr2, i)

class min_max_struct:
    def __init__(self, arr):
        n = len(arr)
        self.min = [[0, i] for i in range(1, n+1)]
        self.max = [[0, i] for i in range(1, n+1)]
        for i in range(n):
            self.min[i][0] = arr[i]
            self.max[i][0] = arr[i]
        self.min.insert(0, n)
        self.max.insert(0, n)
        build_min_heap(self.min, self.max)
        build_max_heap(self.max, self.min)

    def get_min(self):
        self.min[1], self.min[heap_size(self.min)] = self.min[heap_size(self.min)], self.min[1]
        res = self.min.pop()
        self.min[0] -= 1
        self.max[self.min[1][1]][1] = 1
        self.max[res[1]], self.max[heap_size(self.max)] = self.max[heap_size(self.max)], self.max[res[1]]
        self.max.pop()
        self.max[0] -= 1
        self.min[self.max[res[1]][1]][1] = res[1]
        min_heapify(self.min, self.max, 1)
        max_heapify(self.max, self.min, res[1])
        return res[0]

    def get_max(self):
        self.max[1], self.max[heap_size(self.max)] = self.max[heap_size(self.max)], self.max[1]
        res = self.max.pop()
        self.max[0] -= 1
        self.min[self.max[1][1]][1] = 1
        self.min[res[1]], self.min[heap_size(self.min)] = self.min[heap_size(self.min)], self.min[res[1]]
        self.min.pop()
        self.min[0] -= 1
        self.max[self.min[res[1]][1]][1] = res[1]
        max_heapify(self.max, self.min, 1)
        min_heapify(self.min, self.max, res[1])
        return res[0]

    def insert(self, x):
        self.max[0] += 1
        self.min[0] += 1
        self.max.insert(1, [x, 1])
        self.min.insert(1, [x, 1])
        max_heapify(self.max, self.min, 1)
        min_heapify(self.min, self.max, 1)


heaps = min_max_struct([32,4,6,5,22,5,43,77,65,3,4,21,3])
print(heaps.min)
print(heaps.max)
print(heaps.get_max())
print(heaps.get_min())
print(heaps.min)
print(heaps.max)
heaps.insert(98)
heaps.insert(34)
print(heaps.min)
print(heaps.max)