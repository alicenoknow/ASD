class Node:
    def __init__(self, p=None):
        self.preffix = p
        self.list = []      # indeksy wyrazow
        self.succ = []      # nastepne preffixy


def sort_sec(val):
    return val[1]


class SuffixTrie:
    def __init__(self):
        self.root = Node()

    def add(self, node, word, i):
        if i == len(word[1]):
            return
        node.list.append(word[0])
        for j in range(len(node.succ)):
            if word[1][i] == node.succ[j].preffix:
                self.add(node.succ[j], word, i+1)
                return
        x = Node(word[1][i])
        node.succ.append(x)
        self.add(x, word, i+1)

    def build(self, priority, words):
        N = len(words)
        P = [[idx, priority[idx]] for idx in range(N)]
        P.sort(key=sort_sec)

        for i in range(N):
            idx = P[i][0]
            self.add(self.root, [idx, words[idx]], 0)

    def query(self, node, word, k, i, W):
        if i == len(word):
            for i in range(k):
                if i < len(node.list):
                    print(W[node.list[i]])
            return
        for j in range(len(node.succ)):
            if word[i] == node.succ[j].preffix:
                self.query(node.succ[j], word, k, i + 1, W)
        return


P = [2,3,6,7,4,5]
W = ["aab", "dofs", "fasudf", "dosda", "dosdfi", "atr"]

ST = SuffixTrie()
ST.build(P, W)
ST.query(ST.root, "do", 3, 0, W)
