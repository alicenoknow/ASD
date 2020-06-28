'''
Oprocz tablicy z wartosciami, buduję takze drzewo w którym liscie to elementy tablicy a kazdy parent przechowuje sume
swoich dzieci, dzięki temu po aktualizacji wartosci w lisciu wszystkie sumy w których dany lisci miał udzial sa w czasie
logarytmicznym
'''


class Node():
    def __init__(self, sum = 0):
        self.sum = sum
        self.parent = None
        self.left = None
        self.right = None


class Tree():
    def create(self, root, nodes):
        n = len(nodes)
        if n < 3:
            root.left = nodes[0]
            nodes[0].parent = root
            if n == 2:
                root.right = nodes[1]
                nodes[1].parent = root
        else:
            root.left = Node()
            root.left.parent = root
            root.right = Node()
            root.right.parent = root
            self.create(root.left, nodes[:n//2])
            self.create(root.right, nodes[n//2:])

    def __init__(self, nodes):
        self.root = Node()
        self.create(self.root, nodes)


class IntervalSums:
    def __init__(self, n):
        self.table = [0 for _ in range(n)]
        self.nodes = [Node(self.table[i]) for i in range(n)]
        self.tree = Tree(self.nodes)


    def set( self, i, val ):
        dif = val - self.table[i]
        self.table[i] = val
        node = self.nodes[i]
        while node.parent is not None:
            node.sum += dif
            node = node.parent
        self.tree.root.sum += dif

    def interval( self, i, j ):
        diff = 0
        left = self.nodes[i]
        right = self.nodes[j]
        while left.parent is not None and right.parent is not None and left != right:
            if left == left.parent.right:
                diff += left.parent.left.sum
            left = left.parent
            if right == right.parent.left:
                diff += right.parent.right.sum
            right = right.parent

        return left.sum - diff


IS = IntervalSums(4) # tworzy tablicę [0,0,0,0]
IS.set(0,10) # [10,0,0,0]
IS.set(2,-2) # [10,0,-2,0]
IS.set(3,1) # [10,0,-2,1]
print(IS.interval(0,3)) # zwraca 10+0+(-2)+1 = 9
print(IS.interval(1,2) )# zwraca 0-2 = -2