import random


def insert_sort(t):
	for i in range(1, len(t)):
		key = t[i]
		j = i - 1
		while j >= 0 and t[j] > key:
			t[j+1] = t[j]
			j -= 1
		t[j+1] = key


t = [random.randint(1,100) for _ in range(30)]
print(t)
insert_sort(t)
print(t)
