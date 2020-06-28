'''
Spadające klocki jaki poziom
'''

class Node:
    def __init__(self):
        self.low = None
        self.high = None
        self.left = None
        self.right = None
        self.parent = None
        self.level = 0


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
            print(" l: ", node.low, " h: ", node.high, " lvl: ", node.level)
            self.print(node.left)
            self.print(node.right)

    def find_max(self, node, l, h, M):
        if node is None:
            return M
        if l > node.high or h < node.low:
            return M
        if l <= node.low and h >= node.high:
            M = max(node.level, M)
        return max(M, self.find_max(node.left, l, h, M), self.find_max(node.right, l, h, M))

    def insert_interval(self, l, h):
        M = self.find_max(self.root, l, h, 0)
        self._insert(self.root, l, h, M+1)

    def _insert(self, node, l, h, M):
        if node is None:
            return
        if l > node.high or h < node.low:
            return
        if l <= node.low and h >= node.high:
            node.level = M
        self._insert(node.left, l, h, M)
        self._insert(node.right, l, h, M)
        if node.left is not None and node.right is not None:
            node.level = max(node.left.level, node.right.level)





A = [1,2,4,5,6,7,13,18]
T = SegmentTree()
T.create_tree(T.root, A, 0, 7)
T.insert_interval(4, 13)
T.insert_interval(1, 2)
T.insert_interval(4, 18)
T.insert_interval(13, 18)
T.insert_interval(2, 7)

print(T.root.level)
