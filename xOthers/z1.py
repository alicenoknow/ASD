# Alicja Niewiadomska
'''
Algorytm działa podobnie do DFS, odwiedzamy po kolei wierzchołki, jeśli któreś dziecko nie było jeszcze odwiedzone
( ma max_path_one = -inf ) to najpierw odwiedzamy je i jego ewentualne dzieci w głąb, dla kazdego węzła obliczamy
max_path_one - maksymalna ścieżka, która kończy się w obecnym wierzchołku i może być rozszerzana przez jego rodzica
oraz obliczamy max_path_two - maksymalna ścieżka, która zawraca w obecnym wierzchołku - czyli taka która jest
połączeniem dwóch ścieżek prowadzących w głąb dzieci danego wierzchołka i nie może zostać przedłużona
Złożoność: O (V + E)
'''


class Node:
    def __init__( self ):
        self.children = 0
        self.child = []
        self.max_path_one = -float("inf")
        self.max_path_two = -float("inf")



def visit(node):
    if node.children == 0:
        node.max_path_one = 0
        node.max_path_two = 0
    for child in node.child:
        if child[0].max_path_one == -float("inf"):
            visit(child[0])
        node.max_path_two = max(node.max_path_two, node.max_path_one + child[0].max_path_one + child[1])
        node.max_path_one = max(node.max_path_one, child[0].max_path_one + child[1], 0)




def heavy_path(T):
    path = -float("inf")
    for node in T:
        if node.max_path_one == -float("inf"):
            visit(node)
        path = max(path, node.max_path_two, node.max_path_one)
    return path








A = Node()
B = Node()
C = Node()
D = Node()
E = Node()
F = Node()
A.children = 3
A.child = [ (B,5), (C,-1), (F, 8) ]
B.children = 1
B.child = [(D, -2)]
C.children = 0
C.child = [(E, 3)]

T = [A, B, C, D, E]
print(heavy_path(T))
