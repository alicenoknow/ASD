class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

class Stack:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return not self.head

    def push(self, data):
        self.head = Node(data, next=self.head)

    def pop(self):
        if self.is_empty():
            raise Exception("stack is empty")
        data = self.head.data
        self.head = self.head.next
        return data

def partition(arr, l, r):
    pivot = arr[l]
    i = l-1
    j = r+1
    while True:
        j -= 1
        i += 1
        while arr[j] > pivot :  j -= 1
        while arr[i] < pivot :  i += 1
        if i<j: arr[i], arr[j] = arr[j], arr[i]
        else: return j

def QuickSort(A,i,j):
    stack = Stack()
    stack.push(i)
    stack.push(j)
    while not stack.is_empty():
        b = stack.pop()
        a = stack.pop()
        q = partition(A,a,b)
        if a < q-1:
            stack.push(a)
            stack.push(q-1)
        if q+1 < b:
            stack.push(q+1)
            stack.push(b)


arr = [1,45,7,4,867,233,78,93,46,9,2,55,797,9,243,4656,7,78,66,8]
QuickSort(arr,0,len(arr)-1)
print(arr)