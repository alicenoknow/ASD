'''
wejście: graf ważony skierowany o nieujemnych wagach
złożoność dla list adjacencji: O(E * log(V))
złożoność dla macierzy adjacencji: O(V * log(V))
'''


def left_child(i): return 2*i
def right_child(i): return 2*i + 1
def parent(i): return i//2
def heap_size(arr): return arr[0]
def min_heapify(arr, i):
    l = left_child(i)
    r = right_child(i)
    min = i
    if l <= heap_size(arr) and arr[l][0] < arr[min][0]: min = l
    if r <= heap_size(arr) and arr[r][0] < arr[min][0]: min = r
    if min != i:
        arr[min], arr[i] = arr[i], arr[min]
        min_heapify(arr, min)


def build_min_heap(arr):
    arr.insert(0, len(arr))
    for i in range(heap_size(arr)//2, 0, -1):
        min_heapify(arr, i)


def extract_min(arr):
    res = arr[1]
    arr[1], arr[heap_size(arr)] = arr[heap_size(arr)], arr[1]
    arr[0] -= 1
    min_heapify(arr, 1)
    return res


def dijkstra(G, s, P):
    d = [[float("inf"), i] for i in range(len(G))]
    d[s][0] = 0
    Q = []
    for i in range(0, len(G)):
        Q.append(d[i])
    build_min_heap(Q)
    while Q[0]:
        u = extract_min(Q)
        for v in range(len(G[u[1]])):
            if G[u[1]][v] is not None:
                if d[v][0] > u[0] + G[u[1]][v]:
                    d[v][0] = u[0] + G[u[1]][v]
                    P[v].append(u[1])
    for i in range(0, len(G)):
        P[i].append(i)
        print(d[i][0], P[i])




G = [[None, 32, 72, 4, None],
     [None, None, 4, None, None],
     [2, 42, None, 52, 532],
     [2, 1, 4, None, 1],
     [1, 5, 1, 4, None]]
path = [[] for _ in range(len(G))]
dijkstra(G, 1, path)