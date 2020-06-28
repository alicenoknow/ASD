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


def wysz_interp(t, x):
	idx = -1
	p = 0
	k = len(t)-1
	while t[p] <= x <= t[k]:
		sr = p + ((x - t[p])*(k-p)//(t[k]-t[p]))
		if t[sr] == x:
			return sr
		if x < t[sr]:
			k = sr-1
		else:
			p = sr+1


def wysz_interp_rec(t,x,p = 0, k = 29):
	if p > k: return None
	sr = p + ((x - t[p])*(k-p)//(t[k]-t[p]))
	if t[sr] == x: return sr
	if t[sr] > x: return wysz_interp_rec(t,x, 0, sr-1)
	else: return wysz_interp_rec(t,x, sr+1, k)



t = [random.randint(1,100) for _ in range(30)]
quick_sort(t,0,len(t)-1)
print(t)
print(wysz_interp_rec(t,69))
print(t)
