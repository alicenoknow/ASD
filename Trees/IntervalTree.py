'''
wstawia przedziały do drzewa i sprawdza czy jest jakies przeciecie albo znajduje wszystkie przeciecia
'''

class Node:
    def __init__(self, l = None, h = None):
        self.left = None
        self.right = None
        self.maxend = None
        self.parent = None
        self.low = l
        self.high = h

class IntervalST:
    def __init__(self):
        self.root = None

    def insert(self, l, h):
        x = Node(l,h)
        x.maxend = h
        if self.root is None:
            self.root = x
            self.root.maxend = self.root.high
            return
        curr = self.root
        while True:
            if x.low < curr.low:
                if curr.left is None:
                    x.parent = curr
                    curr.left = x
                    curr.left.maxend = curr.left.high
                    return
                else:
                    curr.maxend = max(curr.maxend, x.maxend)
                    curr = curr.left
            elif x.low > curr.low:
                if curr.right is None:
                    x.parent = curr
                    curr.right = x
                    curr.right.maxend = curr.right.high
                    return
                else:
                    curr.maxend = max(curr.maxend, x.maxend)
                    curr = curr.right
            else:
                curr.maxend = max(curr.maxend, x.maxend)
                curr = curr.right

    def any_intersect(self, l, h):
        curr = self.root
        while curr is not None:
            if curr.low <= l and curr.high >= h or curr.low <= l and curr.high >= l or curr.low <= h and curr.high >= h:
                return curr
            elif curr.low < l:
                curr = curr.right
            else:
                curr = curr.left
        return None

    def all_intersections(self, root, l, h, res):
        if root is None:
            return
        if intersect(root.low, root.high, l, h):
            res.append((root.low, root.high))
        if root.left is not None and root.left.maxend >= l:
            self.all_intersections(root.left, l, h, res)
        if root.right is not None and root.right.low >= l:
            self.all_intersections(root.right, l, h, res)



def intersect(l1, h1, l2, h2):
    if h2 < l1 or l2 > h1:
        return False
    return True



I = IntervalST()
I.insert(4,5)
I.insert(2,6)
I.insert(6,9)
I.insert(4,5)
res = []
I.all_intersections(I.root, 0, 10, res)
print(res)