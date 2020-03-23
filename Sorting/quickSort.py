import random


def quick_sort(t, l, r):
	if l >= r: return
	a, b = l, r
	pivot = t[(a+b) >> 1]
	while a <= b:
		while t[a] < pivot: a += 1
		while t[b] > pivot: b -= 1
		if a <= b:
			t[a], t[b] = t[b], t[a]
			a, b = a + 1, b - 1
	quick_sort(t, l, b)
	quick_sort(t, a, r)


t = [random.randint(1, 100) for _ in range(30)]
print(t)
quick_sort(t, 0, 29)
print(t)
