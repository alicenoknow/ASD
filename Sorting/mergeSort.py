import random

def merge_sort(tab):
	if len(tab) > 1:
		m = len(tab)//2
		L = tab[:m]
		R = tab[m:]
		merge_sort(L)
		merge_sort(R)

		i = j = k = 0
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				tab[k] = L[i]
				i += 1
			else:
				tab[k] = R[j]
				j += 1
			k += 1
		while i < len(L):
			tab[k] = L[i]
			k,i = k+1, i+1
		while j < len(R):
			tab[k] = R[j]
			k,j = k+1, j+1



t = [random.randint(1,100) for _ in range(30)]
print(t)
merge_sort(t)
print(t)