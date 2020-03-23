import random

def get_gap(gap):
	gap = (gap*10)//13
	if gap > 1 : return gap
	else: return 1

def comb_sort(tab):
	gap = len(tab)
	swapped = True
	while gap != 1 and swapped:
		gap = get_gap(gap)
		swapped = False
		for i in range(len(t)-gap):
			if tab[i] > tab[i+gap]:
				tab[i],tab[i+gap] = tab[i+gap], tab[i]
				swapped = True


t = [random.randint(1,100) for _ in range(30)]
print(t)
comb_sort(t)
print(t)