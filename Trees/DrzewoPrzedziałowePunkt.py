'''
Drzewo przedzialowe, znajduje przedzialy z zadanym punktem
'''

class Node:
    def __init__(self):
        self.compartments = []
        self.low = None
        self.high = None
        self.left = None
        self.right = None
        self.parent = None


class SegmentTree:
    def __init__(self):
        self.root = Node()

    def create_tree(self, node, array, l, h):
        N = h-l+1
        if N > 1:
            node.left = Node()
            node.left.parent = node
            node.right = Node()
            node.right.parent = node
            self.create_tree(node.left, array, l, (l+h)//2)
            self.create_tree(node.right, array, (l+h+1)//2, h)
            node.low = node.left.low
            node.high = node.right.high
        else:
            node.low = array[l]
            node.high = array[h]


    def print(self, node):
        if node is not None:
            print( " l: ", node.low, " h: ", node.high, " list: ", node.compartments)
            self.print(node.left)
            self.print(node.right)


    def insert_intervals(self, node, l, h):
        if l <= node.low and h >= node.high:
            node.compartments.append((l,h))
            return
        if l > node.high or h < node.low:
            return
        self.insert_intervals(node.left, l, h)
        self.insert_intervals(node.right, l, h)

    def count_comp(self, node, P):
        if node is None: return 0
        if node.low <= P <= node.high:
            return len(node.compartments) + self.count_comp(node.left, P) + self.count_comp(node.right, P)
        if P > node.high or P < node.low:
            return 0


A = [1,2,4,5,6,7,13,18]
T = SegmentTree()
T.create_tree(T.root, A, 0, 7)
T.insert_intervals(T.root, 4,13)
T.insert_intervals(T.root, 1,4)
T.insert_intervals(T.root, 4,18)
T.insert_intervals(T.root, 6,18)
T.insert_intervals(T.root, 2,7)
T.print(T.root)
print(T.count_comp(T.root, 6))
