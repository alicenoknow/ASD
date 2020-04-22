def tasks(A):
	A.sort(key=lambda tup: tup[1])		# sortowanie po czasie zakonczenia aktywnosci
	n = len(A)
	time = 0							# aktualny czas zaczynamy od 0
	act = 0								# licznik aktywnosci
	for i in range(n):
		if time <= A[i][0]:				# jesli godzina rozpoczecia Ai <= niz aktualny czas to wybieramy te aktywnosc
			act += 1					# dodajemy 1 do act
			time = A[i][1]				# time oznacza teraz ktora mamy godzine po ukonczeniu ostatniej aktywnosci
	return act							


print(tasks([(0, 10), (10, 20),(10, 14), (16, 20),  (5, 15)]))
