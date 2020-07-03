def l_child(i):
    return i*2


def r_child(i):
    return i*2 + 1


def parent(i):
    return i//2


def size(tab):
    return tab[0]


def heapify(tab, i):
    l = l_child(i)
    r = r_child(i)
    max = i
    if l <= size(tab) and tab[l] < tab[max]: max = l
    if r <= size(tab) and tab[r] < tab[max]: max = r
    if max != i:
        tab[i], tab[max] = tab[max], tab[i]
        heapify(tab, max)


def build_heap(tab):
    for i in range(size(tab)//2, 0, -1):
        heapify(tab,i)


def huffman_len(A):
    min_heap = A
    cost = 0
    n = len(A)
    min_heap.insert(0, n)
    build_heap(min_heap)                    # budujemy kopiec min
    print(min_heap)
    while size(min_heap) > 1:
        min1 = min_heap[1]                  # usuwamy z niego najmniejszy element
        min_heap[1], min_heap[size(min_heap)] = min_heap[size(min_heap)], min_heap[1]
        min_heap[0] -= 1
        heapify(min_heap, 1)                # naprawiamy kopiec
        min2 = min_heap[1]                  # usuwamy z niego najmniejszy element
        min_heap[1], min_heap[size(min_heap)] = min_heap[size(min_heap)], min_heap[1]
        min_heap[0] -= 1
        heapify(min_heap, 1)                # naprawiamy kopiec
        min_heap[size(min_heap) + 1] = min1 + min2      # dodajemy do kopca sume elementow
        min_heap[0] += 1                    
        cost += min1 + min2                 # dodajemy do kosztu sume dwóch najmniejszych elementow, nie bedziemy sie juz
    return cost                             # nimi bezposrednio zajmowac, zostaly "przykryte" przez nasz nowy
                                            # element (min1 + min2)


