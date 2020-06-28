class Node:
    def __init__(self, k=None, v=None):
        self.key = k
        self.value = v
        self.left = None
        self.right = None
        self.height = 1


class AVL:
    def __init__(self):
        self.root = None

    def insert(self, curr, k, v, p):
        if not curr:
            curr = Node(k, v)
            curr.parent = p
            return curr
        elif k < curr.key:
            curr.left = self.insert(curr.left, k, v, curr)
        else:
            curr.right = self.insert(curr.right, k, v, curr)

        curr.height = 1 + max(self.get_height(curr.left), self.get_height(curr.right))
        balance = self.get_balance(curr)

        if balance > 1 and k < curr.left.key:
            return self.right_rotate(curr)
        if balance < -1 and k > curr.right.key:
            return self.left_rotate(curr)
        if balance > 1 and k > curr.left.key:
            curr.left = self.left_rotate(curr.left)
            return self.right_rotate(curr)
        if balance < -1 and k < curr.right.key:
            curr.right = self.right_rotate(curr.right)
            return self.left_rotate(curr)
        return curr

    def left_rotate(self, node):
        mid = node.right
        node.right = mid.left
        if mid.left is not None:
            mid.left.parent = node
        mid.parent = node.parent
        if not node.parent:
            self.root = mid
        elif node == node.parent.right:
            node.parent.right = mid
        else:
            node.parent.left = mid
        mid.left = node
        node.parent = mid
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        mid.height = 1 + max(self.get_height(mid.left), self.get_height(mid.right))
        return mid

    def right_rotate(self, node):
        mid = node.left
        node.left = mid.right
        if mid.right is not None:
            mid.right.parent = node
        mid.parent = node.parent
        if not node.parent:
            self.root = mid
        elif node == node.parent.left:
            node.parent.left = mid
        else:
            node.parent.right = mid
        mid.right = node
        node.parent = mid
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        mid.height = 1 + max(self.get_height(mid.left), self.get_height(mid.right))
        return mid

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def printTree(self, curr):
        if curr is not None:
            self.printTree(curr.left)
            print(curr.value)
            self.printTree(curr.right)


T = AVL()
T.root = T.insert(T.root, 20, "A", None)
T.root = T.insert(T.root, 200, "S", None)
T.root = T.insert(T.root, 202, "T", None)
T.root = T.insert(T.root, 240, "H", None)
T.root = T.insert(T.root, 230, "G", None)
T.root = T.insert(T.root, 233, "F", None)
T.root = T.insert(T.root, 281, "E", None)
T.root = T.insert(T.root, 224, "D", None)
T.root = T.insert(T.root, 209, "C", None)
T.root = T.insert(T.root, 120, "B", None)

