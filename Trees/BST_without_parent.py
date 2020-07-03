class Node:
    def __init__(self, k=None):
        self.left = None
        self.right = None
        self.key = k


class BST:
    def __init__(self):
        self.root = None

    def insert(self, curr, key):
        if not curr:
            curr = Node(key)
            return curr
        elif key < curr.key:
            curr.left = self.insert(curr.left, key)
        else:
            curr.right = self.insert(curr.right, key)
        return curr

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

    def min_k(self, curr):
        if curr is None:
            return
        while curr.left is not None:
            curr = curr.left
        return curr

    def max_k(self, curr):
        if curr is None:
            return
        while curr.right is not None:
            curr = curr.right
        return curr

    def remove(self, key, curr):
        if not curr:
            return curr
        if key < curr.key:
            curr.left = self.remove(key, curr.left)
        elif key > curr.key:
            curr.right = self.remove(key, curr.right)
        else:
            if not curr.left:
                tmp = curr.right
                curr = None
                return tmp
            if not curr.right:
                tmp = curr.left
                curr = None
                return tmp
            tmp = self.min_k(curr.right)
            curr.key = tmp.key
            curr.right = self.remove(tmp.key, curr.right)
        return curr

    def in_order(self, curr, arr):
        if curr:
            self.in_order(curr.left, arr)
            arr.append(curr.key)
            self.in_order(curr.right, arr)

    def print_tree(self, curr):
        if curr:
            self.print_tree(curr.left)
            print(curr.key)
            self.print_tree(curr.right)

    def average(self):
        S, C = _average(self.root)
        return S / C


def _average(node):
    if not node.left and not node.right:
        return node.key, 1
    Ls = Rs = Lcnt = Rcnt = 0
    if node.left:
        Ls, Lcnt = _average(node.left)
    if node.right:
        Rs, Rcnt = _average(node.right)
    return (Ls + Rs + node.key), (Lcnt + Rcnt + 1)


def serialize(root, serial):
    if root is not None:
        serial.append((root.key))
        serialize(root.left, serial)
        serialize(root.right, serial)
    else:
        serial.append('x')


def deserialize(serial):
    if serial[0] == 'x':
        serial.pop(0)
        return None
    else:
        if len(serial) > 0:
            node = serial.pop(0)
            newroot = Node(node)
            newroot.left = deserialize(serial)
            newroot.right = deserialize(serial)
            return newroot


def merge_lists(L1, L2):
    merged = []
    i, j = 0, 0
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            merged.append(L1[i])
            i += 1
        elif L1[i] == L2[j]:
            i += 1
        else:
            merged.append(L2[j])
            j += 1
    return merged + L1[i:] + L2[j:]


def create_balanced_tree(A, s, t, curr):
    if s == t:
        return None
    m = (s + t)//2
    curr = Node(A[m])
    curr.left =  create_balanced_tree(A, s, m, curr.left)
    curr.right = create_balanced_tree(A, m+1, t, curr.right)
    return curr


def merge_trees(T1, T2):
    A1 = []
    A2 = []
    T1.in_order(T1.root, A1)
    T2.in_order(T2.root, A2)
    A = merge_lists(A1, A2)
    new_tree = BST()
    new_tree.root = create_balanced_tree(A, 0, len(A)-1, new_tree.root)
    new_tree.print_tree(new_tree.root)
    return new_tree


T = BST()
T.root = T.insert(T.root, 12)
T.root = T.insert(T.root, 8)
T.root = T.insert(T.root, 122)
T.root = T.insert(T.root, 1)
T.root = T.insert(T.root, 2)


T1 = BST()
T1.root = T1.insert(T1.root, 121)
T1.root = T1.insert(T1.root, 54)
T1.root = T1.insert(T1.root, 12)
T1.root = T1.insert(T1.root, 11)
T1.root = T1.insert(T1.root, 2)

merge_trees(T, T1)