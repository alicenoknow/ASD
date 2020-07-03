class Node:
    def __init__(self, k=None, v=None, p=None):
        self.key = k
        self.value = v
        self.parent = p
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        x = Node()
        x.key = key
        x.value = value
        if self.root is None:
            self.root = x
            return
        curr = self.root
        while True:
            if key < curr.key:
                if curr.left is None:
                    curr.left = x
                    curr.left.parent = curr
                    return
                else:
                    curr = curr.left
            elif key > curr.key:
                if curr.right is None:
                    curr.right = x
                    curr.right.parent = curr
                    return
                else:
                    curr = curr.right
            else:
                return

    def find(self, key):
        curr = self.root
        while curr is not None:
            if curr.key == key:
                return curr
            elif curr.key < key:
                curr = curr.right
            else:
                curr = curr.left
        return None

    def min_k(self):
        curr = self.root
        if curr is None:
            return
        while curr.left is not None:
            curr = curr.left
        return curr

    def max_k(self):
        curr = self.root
        if curr is None:
            return
        while curr.right is not None:
            curr = curr.right
        return curr

    def succ(self, key):
        curr = self.find(key)
        if curr is None:
            return None
        if curr.right is not None:
            curr = curr.right
            while curr.left is not None:
                curr = curr.left
            return curr
        else:
            while curr.parent is not None and curr.parent.right == curr:
                curr = curr.parent
            return curr.parent
        return None

    def pred(self, key):
        curr = self.find(key)
        if curr is None:
            return None
        if curr.left is not None:
            curr = curr.left
            while curr.right is not None:
                curr = curr.right
            return curr
        else:
            while curr.parent is not None and curr.parent.left == curr:
                curr = curr.parent
            return curr.parent
        return None

    def remove(self, key):
        curr = self.find(key)
        if curr is None:
            return
        if curr.left is None:
            tmp = curr.right
            if curr.parent.left == curr:
                curr.parent.left = tmp
            else:
                curr.parent.right = tmp
            tmp.parent = curr.parent
            curr = None
            return
        elif curr.right is None:
            tmp = curr.left
            if curr.parent.left == curr:
                curr.parent.left = tmp
            else:
                curr.parent.right = tmp
            tmp.parent = curr.parent
            curr = None
            return
        else:
            succ = self.succ( key)
            curr.key, succ.key, curr.value, succ.value = succ.key, curr.key, succ.value, curr.value
            self.remove(key)

    def printTree(self, curr):
        if curr is not None:
            self.printTree(curr.left)
            print(curr.value)
            self.printTree(curr.right)

    def average(self):
        S, C = _average(self.root)
        return S / C


def _average(node):
    if not node.left and not node.right:
        return node.value, 1
    Ls = Rs = Lcnt = Rcnt = 0
    if node.left:
        Ls, Lcnt = _average(node.left)
    if node.right:
        Rs, Rcnt = _average(node.right)
    return (Ls + Rs + node.value), (Lcnt + Rcnt + 1)


def serialize(root, serial):
    if root is not None:
        serial.append((root.key, root.value))
        serialize(root.left, serial)
        serialize(root.right, serial)
    else:
        serial.append('x')


def deserialize(serial, p):
    if serial[0] == 'x':
        serial.pop(0)
        return None
    else:
        if len(serial) > 0:
            node = serial.pop(0)
            newroot = Node(node[0], node[1], p)
            newroot.left = deserialize(serial, newroot)
            newroot.right = deserialize(serial, newroot)
            return newroot




D = BST()
D.insert(10, "A")
D.insert(12, "B")
D.insert(15, "G")
D.insert(6, "F")
D.insert(21, "E")
D.insert(11, "D")
D.insert(8, "C")
D.insert(1, "H")
D.remove(6)
b = D.pred(10)
print("pred: ", b.value)
D.printTree(D.root)
res = []
serialize(D.root, res)
ND = BST()
print("=============")
ND.root = deserialize(res, None)
ND.printTree(ND.root)
b = ND.pred(12)
print("pred: ", b.value)


#+++++++++++++++++++++++++++++++++++++++++++

def mid(A, s ,t):
    if s == t:
        return
    m = (s + t)//2
    print(A[m])
    mid(A, s, m)
    mid(A, m+1, t)