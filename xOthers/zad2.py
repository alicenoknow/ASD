#Alicja Niewiadomska
'''
Idea: wykonuje dwukrotnie algorytm podobny do select(ktory zwracał indeks k-tego najmniejszego elementu w tablicy),
jednak bez samego zwracanie wartosci a jedynie ustawia k-ty elemnt na swojej pozycji i przerzuca wszystkie mniejsze
od niego na prawo a większe na lewo. najpierw algorytm wykonuje dal całej tablicy wzgledem indeksu p, wiem wtedy, że
wszyscy żołnierze nizsi od T[p](w posortowanym ustawieniu) są na prawo, nastepnie powtarzam algorytm dla zakresu od p
do końca tablicy wzgledem q, wiem wtedy że wszyscy wyzsi od T[q](w posortowanym ustawieniu) są na lewo do q i na prawo
od p, ponieważ część tablicy < p nie była brana pod uwagę w drugim wykoaniu, dlatego teraz miedzy indeksami p i q
znajduja sie wartosci takie jakie byłyby w posortowanej tablicy miedzy indeksami p i q. Przepisuje je do tablicy wynikowej
Złożoność to O(n) ponieważ taka złozonosc ma algorytm select

'''

def partition(arr, l, r):
    pivot = arr[l]
    i = l-1
    j = r+1
    while True:
        j -= 1
        i += 1
        while arr[j] < pivot:  j -= 1
        while arr[i] > pivot:  i += 1
        if i < j: arr[i], arr[j] = arr[j], arr[i]
        else: return j


def select(arr, l, r, i):
    if l == r: return
    p = partition(arr,l,r)
    if p == i: return
    elif p < i:
        select(arr, p + 1, r, i)
        return
    select(arr, l, p-1, i)
    return


def section(T, p, q):
    n = len(T)
    select(T, 0, n-1, p)
    select(T, p, n-1, q)
    result = [T[i] for i in range(p, q+1)]
    return result




