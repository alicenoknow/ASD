import random

def merge_sort(tab):
	if len(tab) <= 1:
		return 0
	else:
		m = len(tab)//2
		L = tab[:m]
		R = tab[m:]
		c1 = merge_sort(L)
		c2 = merge_sort(R)
		res = 0 + c1 + c2
		i = j = k = 0
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				tab[k] = L[i]
				i += 1
			else:
				tab[k] = R[j]
				j += 1
				res += len(L)-i
			k += 1
		while i < len(L):
			tab[k] = L[i]
			k,i = k+1, i+1
		while j < len(R):
			tab[k] = R[j]
			k,j = k+1, j+1
	return res



t = [random.randint(1,100) for _ in range(5)]
print(t)
c = merge_sort(t)
print(c)