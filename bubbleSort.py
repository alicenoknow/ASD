import random


def bubble_sort(t):
	change = True
	last = len(t)-1
	stop = last
	while change:
		change = False
		stop = last
		for j in range(0,stop):
			if t[j] > t[j+1]:
				t[j], t[j+1] = t[j+1], t[j]
				change = True
				last = j

t = [random.randint(1,100) for _ in range(30)]
print(t)
bubble_sort(t)
print(t)
