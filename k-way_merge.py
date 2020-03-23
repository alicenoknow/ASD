def l_child(i):
    return i*2
def r_child(i):
    return i*2 + 1
def parent(i):
    return i//2
def size(tab):
    return tab[0]

def heapify(tab, i):            #min heapify
    l = l_child(i)
    r = r_child(i)
    smallest = i
    if l < size(tab) and tab[l][1] < tab[i][1]:
        smallest = l
    if r < size(tab) and tab[r][1] < tab[smallest][1]:
        smallest = r
    if smallest != i:
        tab[i], tab[smallest] = tab[smallest], tab[i]
        heapify(tab, smallest)

def build_heap(tab):
    i = size(tab)//2
    while i > 0:
        heapify(tab, i)
        i -= 1

def kway_merge(arrays, k = 5, n = 4):                                       #k list, n elements each
    result = [0]*k*n
    min_heap_arr = [k+1, [0, arrays[0].pop(0)],[1,arrays[1].pop(0)],        #array with tuples where [nr of list, smallest element]
                    [2,arrays[2].pop(0)],[3,arrays[3].pop(0)],[4,arrays[4].pop(0)]]
    build_heap(min_heap_arr)                                                #make heap from first elements of k arrays
    for i in range(0, n*k):
        result[i] = min_heap_arr[1][1];                                     #every loop pop out the current smallest element
        if len(arrays[min_heap_arr[1][0]]) > 0:                             #if list is not empty
            min_heap_arr[1][1] = arrays[min_heap_arr[1][0]].pop(0)          #get next element from that list
        else:                                                               #if the list is empty swap it with the last not empty list
            min_heap_arr[1], min_heap_arr[size(min_heap_arr)-1] = min_heap_arr[size(min_heap_arr)-1], min_heap_arr[1]
            min_heap_arr[0] -= 1                                            #decrease list number(size) by 1 and continue with all not empty lists
        heapify(min_heap_arr,1)
    print(result)

arrays = [[4,5,6,8],[1,7,8,9],[1,2,3,4],[4,6,8,9],[1,5,8,9]]
kway_merge(arrays)