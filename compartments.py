'''
Problem: given some compartments, find the minimal number of compartments that contains all given
e.g. given: [2,4], [3,7], [4,5], [1,7]
answer is: 1, we only need [1,7], because all compartments are contained in [1,7]
'''

class Compartment:
    def __init__(self, o , c):
        self.open = o
        self.close = c


class Interval_Tree:
    def __init__(self, x):
        self.comp = x
        self.left = None
        self.right = None


    def add2tree(self, x):
        if x.open <= self.comp.open and x.close >= self.comp.close:
            self.comp = x
        elif x.open < self.comp.open and x.close <= self.comp.close:
            if self.left is None:
                self.left = Interval_Tree(x)
            else:
                self.left.add2tree(x)
        elif x.close > self.comp.close and x.open >= self.comp.open:
            if self.right is None:
                self.right = Interval_Tree(x)
            else:
                self.right.add2tree(x)

    def print_tree(self):
        if self.left is not None:
            self.left.print_tree()
        if self.right is not None:
            self.right.print_tree()
        print("[", self.comp.open, ",", self.comp.close, "]")


def fmc(arr):                       # find minimum number of compartments to cover whole values
    tree = Interval_Tree(arr[0])
    for i in range(1, len(arr)):
        tree.add2tree(arr[i])
    tree.print_tree()


a = Compartment(2, 7)
b = Compartment(1, 2)
c = Compartment(4, 6)
d = Compartment(2, 5)
e = Compartment(6, 8)
f = Compartment(3, 5)
g = Compartment(3, 6)
h = Compartment(1, 2)
arr = [a,b,c,d,e,f,g,h]
fmc(arr)
