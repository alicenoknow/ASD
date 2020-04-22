'''
Problem: design data structure that allows operations insert() and get_median() in O(log N)
Idea: split array into two heaps for first half with smaller numbers create max heap, for half containing bigger numbers
create min heap, a median will always be in root of max heap
'''

def left_child(i): return 2*i
def right_child(i): return 2*i + 1
def parent(i): return i//2
def heap_size(arr): return arr[0]


def max_heapify(arr, i):
    l = left_child(i)
    r = right_child(i)
    max = i
    if l <= heap_size(arr) and arr[l] > arr[max]: max = l
    if r <= heap_size(arr) and arr[r] > arr[max]: max = r
    if max != i:
        arr[max], arr[i] = arr[i], arr[max]
        max_heapify(arr, max)


def build_max_heap(arr):
    for i in range(heap_size(arr)//2, 0, -1):
        max_heapify(arr, i)


def min_heapify(arr, i):
    l = left_child(i)
    r = right_child(i)
    min = i
    if l <= heap_size(arr) and arr[l] < arr[min]: min = l
    if r <= heap_size(arr) and arr[r] < arr[min]: min = r
    if min != i:
        arr[min], arr[i] = arr[i], arr[min]
        min_heapify(arr, min)


def build_min_heap(arr):
    for i in range(heap_size(arr)//2, 0, -1):
        min_heapify(arr, i)


class Double_Heap:
    def __init__(self):
        self.max_heap = [0]
        self.min_heap = [0]

    def insert_value(self, value):
        if self.max_heap[0] == 0:
            self.max_heap.append(value)
            self.max_heap[0] += 1
        elif self.max_heap[1] > value:
            self.max_heap.append(value)
            self.max_heap[0] += 1
        else:
            self.min_heap.append(value)
            self.min_heap[0] += 1

        if heap_size(self.max_heap) > heap_size(self.min_heap) + 1:
            self.min_heap.append(self.max_heap[1])
            self.min_heap[0] += 1
            self.min_heap[1], self.min_heap[heap_size(self.min_heap)] = self.min_heap[heap_size(self.min_heap)],  self.min_heap[1]
            self.max_heap[1] = self.max_heap[heap_size(self.max_heap)]
            del self.max_heap[-1]
            self.max_heap[0] -= 1
            max_heapify(self.max_heap, 1)
            min_heapify(self.min_heap, 1)

        elif heap_size(self.max_heap) < heap_size(self.min_heap):
            self.max_heap.append(self.min_heap[1])
            self.max_heap[0] += 1
            self.max_heap[1], self.max_heap[heap_size(self.max_heap)] = self.max_heap[heap_size(self.max_heap)], self.max_heap[1]
            self.min_heap[1] = self.min_heap[heap_size(self.min_heap)]
            self.min_heap[0] -= 1
            del self.min_heap[-1]
            min_heapify(self.min_heap, 1)
            max_heapify(self.max_heap, 1)



    def get_median(self):
        self.max_heap[1], self.max_heap[heap_size(self.max_heap)] = self.max_heap[heap_size(self.max_heap)], self.max_heap[1]
        med = self.max_heap.pop()
        self.max_heap[0] -= 1
        if heap_size(self.max_heap) < heap_size(self.min_heap):
            self.max_heap.append(self.min_heap[1])
            self.max_heap[0] += 1
            self.max_heap[1], self.max_heap[heap_size(self.max_heap)] = self.max_heap[heap_size(self.max_heap)], \
                                                                        self.max_heap[1]
            self.min_heap[1] = self.min_heap[heap_size(self.min_heap)]
            self.min_heap[0] -= 1
            del self.min_heap[-1]
            min_heapify(self.min_heap, 1)
        max_heapify(self.max_heap, 1)
        return med


test = Double_Heap()

test.insert_value(17)
test.insert_value(1)
test.insert_value(12)
test.insert_value(15)
test.insert_value(22)
test.insert_value(2)
test.insert_value(10)
test.insert_value(54)
test.insert_value(5)
test.insert_value(8)
test.insert_value(32)
print(test.max_heap)
print(test.min_heap)
print(test.get_median())
print(test.max_heap)
print(test.min_heap)