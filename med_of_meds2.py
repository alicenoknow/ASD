import random


def insertsort(t,l,r):
	for i in range(l, r+1):               # without r
		key = t[i]
		j = i - 1
		while j >= l and t[j] > key:
			t[j+1] = t[j]
			j -= 1
		t[j+1] = key

def swap(arr, i1, i2):
    arr[i1], arr[i2] = arr[i2], arr[i1]


def partition(arr, l, r):
    i = l - 1
    pivot = arr[r]
    for j in range(l, r):

        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


def select_five(L, left, right, k):
    # 1. Jeżeli jest mało elementów, to sortuj.
    # p powinno być co najmniej 5, aby ustawiło sie i > 0.
    p = 5   # może być kilkadziesiąt
    if (right-left+1) <= p:
        insertsort(L, left, right)
        return left+k-1   # zwracam indeks
    # 2. Podziel listę na 5-elementowe podzbiory, najwyżej jeden 4-elementowy.
    # 3. Posortuj podzbiory.
    left2 = left
    right2 = left + 4
    i = left   # pierwszy wolny
    while right2 <= right:
        insertsort(L, left2, right2)
        # Przerzucamy mediany na początek tablicy.
        swap(L, i, left2+2)
        i += 1
        left2 += 5
        right2 += 5
    # Tu można posortować zbiory mniej niż 5-elementowe.
    if right2 == right+1 or right2 == right+2:
        insertsort(L, left2, right)
        swap(L, i, left2+1)
        i += 1
    # 5. Wyznaczamy medianę median rekurencyjnie.
    median_idx = select_five(L, left, i-1, (i-left+1)//2)
    # 6. Dalej jak Hoare, mediana będzie punktem podziału.
    swap(L, median_idx, right)   # element podzialu na prawo
    pivot = partition(L, left, right)
    k2 = pivot - left + 1
    if k == k2:
        return pivot   # zwracam indeks
    elif k < k2:
        return select_five(L, left, pivot-1, k)
    else:
        return select_five(L, pivot+1, right, k-k2)


arr = [random.randint(1,100) for _ in range(40)]
print(arr[select_five(arr,0,len(arr)-1, (len(arr)+1)//2)])
print(arr)