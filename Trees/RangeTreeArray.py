'''
Array based tree, range from to
'''

class Tree:
    def __init__(self, A):
        self.tree = [None for _ in range(len(A) * 2)]
        self.build(A, 1, 0, len(A)-1)
        self.size = len(A)

    def build(self, array, i, l, r):
        if l == r:
            self.tree[i] = array[l];
        else:
            mid = (l + r) // 2
            self.build(array, i*2, l, mid)
            self.build(array, i*2+1, mid+1, r)
            self.tree[i] = self.tree[i*2] + self.tree[i*2+1]

    def get_sum(self, fro, to):
        return self._get_sum(1, 0, T.size-1, fro, to)

    def _get_sum(self, i, l, r, fro, to):
        if fro > to:
            return 0
        if fro == l and to == r:
            return self.tree[i]
        mid = (l + r)//2
        return self._get_sum(i*2, l, mid, fro, min(to, mid)) + self._get_sum(i*2+1, mid+1, r, max(fro, mid+1), to)

    def update(self, idx, val):
        self._update(1, 0, self.size -1, idx, val)

    def _update(self, i, l, r, idx, val):
        if l == r:
            self.tree[i] = val
        else:
            mid = (l + r)//2
            if idx <= mid:
                self._update(i*2, l, mid, idx, val)
            else:
                self._update(i*2+1, mid+1, r, idx, val)
            self.tree[i] = self.tree[i*2] + self.tree[i*2+1]


A = [6,7,1,3,2,4,5]
T = Tree(A)
print(T.get_sum(0, 0))
T.update(4, 15)
print(T.get_sum(3, 3))
print(T.tree)