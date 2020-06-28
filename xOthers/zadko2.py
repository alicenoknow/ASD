'''
wejście: graf ważony skierowany o nieujemnych wagach
złożoność dla list adjacencji: O(E * log(V))
złożoność dla macierzy adjacencji: O(E * log(V))
'''


def left_child(i): return 2*i
def right_child(i): return 2*i + 1
def parent(i): return i//2
def heap_size(arr): return arr[0]
def min_heapify(arr, i):
    l = left_child(i)
    r = right_child(i)
    min = i
    if l <= heap_size(arr) and arr[l][1] < arr[min][1]: min = l
    if r <= heap_size(arr) and arr[r][1] < arr[min][1]: min = r
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


def dijkstra(G, s):
    n = len(G)
    parent = [None for _ in range(n)]
    d = [[i, float("inf")] for i in range(n)]       # array of [distance from source, idx of vertex]
    d[s][1] = 0                                     # d[source] = 0 else inf
    Q = []                                          # queque
    for i in range(0, n):                           # add to queque
        Q.append(d[i])
    build_min_heap(Q)                               # build min heap from Q

    while Q[0]:                                     # while Q is not empty
        u = extract_min(Q)                          # extract vertex with the smallest distance from source
        for v in G[u[0]]:                           # for all adjacent vertexes relax
            if d[v[0]][1] > d[u[0]][1] + v[1]:      # if path through u to v is shortest than current path to v
                d[v[0]][1] = d[u[0]][1] + v[1]      # then change it to shorter
                parent[v[0]] = u[0]
    return parent




G = [[(1,0), (2,1)],
[(3,1), (2,0)],
[(3,0)],
[]]
print( dijkstra( G, 0 ) ) # wypisze [None,0,1,2] -
