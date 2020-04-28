'''
wejście: graf ważony skierowany o nieujemnych wagach
złożoność dla list adjacencji: O(E * log(V))
złożoność dla macierzy adjacencji: O(V * log(V))
'''

class Vertex:
    def __init__(self,idx,d,a):
        self.idx = idx
        self.d = d
        self.adjacent = a

def left_child(i): return 2*i
def right_child(i): return 2*i + 1
def parent(i): return i//2
def heap_size(arr): return arr[0]
def min_heapify(arr, i):
    l = left_child(i)
    r = right_child(i)
    min = i
    if l <= heap_size(arr) and arr[l].d < arr[min].d: min = l
    if r <= heap_size(arr) and arr[r].d < arr[min].d: min = r
    if min != i:
        arr[min], arr[i] = arr[i], arr[min]
        min_heapify(arr, min)


def build_min_heap(arr):
    arr.insert(0, len(arr))
    for i in range(heap_size(arr)//2, 0, -1):
        min_heapify(arr, i)

def initialise(G,s):
    for i in range(len(G)):
        G[i].d = float("inf")
    G[s].d = 0

def extract_min(arr):
    res = arr[1]
    arr[1], arr[heap_size(arr)] = arr[heap_size(arr)], arr[1]
    arr[0] -= 1
    min_heapify(arr, 1)
    return res


def dijkstra(G,s,P):
    initialise(G,s)
    Q = []
    for i in range(0, len(G)):
        Q.append(G[i])
    build_min_heap(Q)
    while Q[0]:
        u = extract_min(Q)
        for v in u.adjacent:
            if G[v[0]].d > u.d + v[1]:
                G[v[0]].d = u.d + v[1]
                P[v[0]].append(u.idx)
    for i in range(0, len(G)):
        P[i].append(G[i].idx)
        print(G[i].d, P[i])




G = [Vertex(0,0,[[1,4],[2,7],[5,6]]),
     Vertex(1,0,[[2,45],[3,12],[5,63]]),
     Vertex(2,0,[[1,3],[0,7],[4,36],[3,5]]),
     Vertex(3,0,[[1,54],[2,57],[0,36],[4,1]]),
     Vertex(4,0,[[1,10],[3,71],[5,6]]),
     Vertex(5,0,[[1,0],[0,7],[3,6]])]
path = [[] for _ in range(len(G))]
dijkstra(G,1, path)