from math import sqrt


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def dist(self):
        return sqrt(self.x * self.x + self.y * self.y)


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
	min = i
	if l <= size(tab) and tab[l].dist() > tab[min].dist(): min = l
	if r <= size(tab) and tab[r].dist() > tab[min].dist(): min = r
	if min != i:
		tab[i], tab[min] = tab[min], tab[i]
		heapify(tab, min)


def build_heap(tab):
	for i in range(size(tab)//2, 0, -1):
		heapify(tab,i)


def heapsort_points(tab):
	tab.insert(0,len(tab))
	build_heap(tab)
	for i in range(size(tab), 1, -1):
		tab[1], tab[size(tab)] = tab[size(tab)], tab[1]
		tab[0] -= 1
		heapify(tab,1)
	tab.remove(tab[0])


a = Point(1,1)
b = Point(2,3)
c = Point(5,2)
d = Point(-1,0)
e = Point(0,0)
f = Point(2,5)
g = Point(10,2)
arr = [a, b, c, d, e, f, g]
heapsort_points(arr)
for i in range(len(arr)):
    print("(", arr[i].x, ",", arr[i].y, ") ")