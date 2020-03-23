import random

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
	if l <= size(tab) and tab[l] > tab[max]: max = l
	if r <= size(tab) and tab[r] > tab[max]: max = r
	if max != i:
		tab[i], tab[max] = tab[max], tab[i]
		heapify(tab, max)

def build_heap(tab):
	for i in range(size(tab)//2, 0, -1):
		heapify(tab,i)
def heap_sort(tab):
	tab.insert(0,len(tab)-1)
	build_heap(tab)
	for i in range(size(tab), 1, -1):
		tab[1], tab[size(tab)] = tab[size(tab)], tab[1]
		tab[0] -= 1
		heapify(tab,1)
	tab.remove(tab[0])

t = [random.randint(1,100) for _ in range(30)]
print(t)
heap_sort(t)
print(t)