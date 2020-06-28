class Node:
    def __init__(self, leaf=False):
        self.keys = []
        self.children = []
        self.leaf = leaf


class Btree:
    def __init__(self, t=3):
        self.root = None
        self.t = t

    def insert(self, key):
        if self.root is None:
            self.root = Node()
            self.root.keys.append(key)
            self.root.leaf = True
            return

        curr = self.root
        if len(curr.keys) == (2 * self.t) - 1:
            newnode = Node()
            self.root = newnode
            newnode.children.insert(0, curr)
            self.split_child(newnode, 0)
            self.insert_nonfull(newnode, key)
        else:
            self.insert_nonfull(curr, key)

    def insert_nonfull(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append(0)
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.children[i].keys) == (2 * self.t) - 1:
                self.split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self.insert_nonfull(x.children[i], k)

    def split_child(self, x, i):
        t = self.t
        y = x.children[i]
        z = Node(leaf=y.leaf)

        x.children.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])

        z.keys = y.keys[t:(2 * t - 1)]
        y.keys = y.keys[0:(t - 1)]

        if not y.leaf:
            z.children = y.children[t:(2 * t)]
            y.children = y.children[0:(t - 1)]

    def get_min(self):
        curr = self.root
        if curr is None:
            return
        while not curr.leaf:
            curr = curr.children[0]
        return curr.keys[0]

    def get_max(self):
        curr = self.root
        if curr is None:
            return
        while not curr.leaf:
            curr = curr.children[len(curr.children) - 1]
        return curr.keys[len(curr.keys) - 1]

    def find(self, node):
        curr = self.root
        while not curr.leaf:
            if node in curr.keys:
                return node
            for i in range(len(curr.keys)):
                if node < curr.keys[i]:
                    curr = curr.children[i]
                    break
            curr = curr.children[len(curr.children) - 1]
        return None

    def pred(self, key):
        curr = self.find(key)
        if curr:
            for i in range(curr.keys-1, -1, -1):
                 if curr.keys[i] < key:
                    curr = curr.children[i]
                    while not curr.leaf:
                        curr = curr.children[0]
                    return curr.keys[0]


T = Btree()
T.insert(5)
T.insert(23)
T.insert(112)
T.insert(12)
T.insert(98)
T.insert(1)
print(T.get_max())