'''
Minimum Range Query array based
'''

class Node:
    def __init__(self):
        self.min = None
        self.low = None
        self.high = None
        self.left = None
        self.right = None
        self.parent = None


class SegmentTree:
    def __init__(self):
        self.root = Node()

    def createTree(self, node, array, l, h):
        N = len(array)
        if N > 1:
            node.left = Node()
            node.left.parent = node
            node.right = Node()
            node.right.parent = node
            self.createTree(node.left, array[:N//2], l, (l+h)//2)
            self.createTree(node.right, array[N//2:], (l+h+1)//2, h)
            node.min = min(node.left.min, node.right.min)
            node.low = node.left.low
            node.high = node.right.high
        else:
            node.min = array[0]
            node.low = l
            node.high = h

    def print(self, node):
        if node is not None:
            print("sum: ", node.sum, " l: ", node.low, " h: ", node.high)
            self.print(node.left)
            self.print(node.right)

    def get_min(self, node, l, h):
        if node.low >= l and node.high <= h:
            return node.min
        if node.low > h or node.high < l:
            return float("inf")
        M = float("inf")
        if node.left is not None:
            M = min(self.get_min(node.left, l, h), M)
        if node.right is not None:
            M = min(self.get_min(node.right, l, h), M)
        return M


A = [6,7,5,1,2,6,17,3]
N = 8
T = SegmentTree()
T.createTree(T.root, A, 0, 7)
s = T.get_min(T.root, 5,7)
print(s)
