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
    d = [[float("inf"), i] for i in range(len(G))]      # array of [distance from source, idx of vertex]
    d[s][0] = 0                                 # d[source] = 0 else inf
    Q = []                                      # queque
    for i in range(0, len(G)):                  # add to queque
        Q.append(d[i])
    build_min_heap(Q)                           # build min heap from Q
    while Q[0]:                                 # while Q is not empty
        u = extract_min(Q)                      # extract vertex with the smallest distance from source
        for v in G[u[1]]:                       # for all adjacent vertexes relax
            if d[v[0]][0] > d[u[0]] + v[1]:     # if path through u to v is shortest than current path to v
                d[v[0]][0] = d[u[0]] + v[1]     # then change it to shorter
                P[v[0]].append(u)               # to print
    for i in range(1, len(G)):
        print(P[1])




G = [ [[1,20],[3,5],[4,0]],
     [[0,1], [2,5]],
     [[1,4],[3,5],[4,1]],
     [[1,3],[2,5],[4,10]],
     [[0,2],[2,4]]]
printing = [[] for _ in range(len(G))]
dijkstra(G,0, printing)