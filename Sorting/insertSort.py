import random


def insert_sort(t):
	for i in range(1, len(t)):
		key = t[i]
		j = i - 1
		while j >= 0 and t[j] > key:
			t[j+1] = t[j]
			j -= 1
		t[j+1] = key

def insertsort_range(t,l,r):
	for i in range(l, r):
		key = t[i]
		j = i - 1
		while j >= l and t[j] > key:
			t[j+1] = t[j]
			j -= 1
		t[j+1] = key


t = [random.randint(1,100) for _ in range(30)]
print(t)
insertsort_range(t,5,10)
print(t)
