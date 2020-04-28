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
        # change values of indexes in second heap
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
        # change values of indexes in second heap
        arr2[arr[min][1]][1], arr2[arr[i][1]][1] = arr2[arr[i][1]][1], arr2[arr[min][1]][1]
        min_heapify(arr,arr2, min)


def build_min_heap(arr, arr2):
    for i in range(heap_size(arr)//2, 0, -1):
        min_heapify(arr, arr2, i)


class MinMaxStruct:
    def __init__(self, arr):
        n = len(arr)
        self.min = [[0, i] for i in range(1, n+1)]
        self.max = [[0, i] for i in range(1, n+1)]
        for i in range(n):
            self.min[i][0] = arr[i]
            self.max[i][0] = arr[i]                     # fill min max with randomly orderd numbers and assign indexes
        self.min.insert(0, n)                           # 0 index - size of heap
        self.max.insert(0, n)
        build_min_heap(self.min, self.max)              # build min max heaps
        build_max_heap(self.max, self.min)

    def get_min(self):
        # swap min value with last value in array
        self.min[1], self.min[heap_size(self.min)] = self.min[heap_size(self.min)], self.min[1]
        # pop min to res
        res = self.min.pop()
        # decrease heap size
        self.min[0] -= 1
        # change index of swapped value in max heap
        self.max[self.min[1][1]][1] = 1
        # in max heap also swap min with last value
        self.max[res[1]], self.max[heap_size(self.max)] = self.max[heap_size(self.max)], self.max[res[1]]
        # pop min
        self.max.pop()
        # decrease heap size
        self.max[0] -= 1
        # change index of swapped vaule in min heap
        self.min[self.max[res[1]][1]][1] = res[1]
        min_heapify(self.min, self.max, 1)                  # fix heaps
        max_heapify(self.max, self.min, res[1])
        return res[0]

    def get_max(self): # same as get_min
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
        self.max.append([x, heap_size(self.max)])
        self.min.append([x, heap_size(self.min)])
        curr = heap_size(self.max)
        # in max heap while x > parent pop up x and change values of indexes
        while curr > 1 and self.max[curr][0] > self.max[parent(curr)][0]:
            self.max[curr], self.max[parent(curr)] = self.max[parent(curr)],  self.max[curr]
            self.min[self.max[curr][1]][1] = parent(curr)
            self.min[self.max[parent(curr)][1]][1] = curr
            curr = parent(curr)
        curr = heap_size(self.min)
        while self.min[curr][0] < self.min[parent(curr)][0]:
            self.min[curr], self.min[parent(curr)] = self.min[parent(curr)], self.min[curr]
            self.max[self.min[curr][1]][1] = parent(curr)
            self.max[self.min[parent(curr)][1]][1] = curr
            curr = parent(curr)


heaps = MinMaxStruct([32,4,6,5,22,5,43,77,65,3,4,21,3])
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