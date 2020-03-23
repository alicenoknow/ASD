import random


def min_idx(t, start):
	minidx  = start
	mint = t[start]
	for i in range(start+1, len(t)):
		if t[i] < mint:
			minidx = i
			mint = t[i]
	return minidx

def selection_sort(t):
	for i in range(0, len(t)-1):
		minidx = min_idx(t,i)
		t[i], t[minidx] = t[minidx], t[i]



t = [random.randint(1,100) for _ in range(30)]
print(t)
selection_sort(t)
print(t)
