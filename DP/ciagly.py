def knapsack(A, k): 							# A[i][0] - profit,  A[i][1] - waga,  k - pojemnosc
	n = len(A)
	profit = 0
	tmp = [[0 for _ in range(2)] for _ in range(n)] 	# tworzymy dwuwymiarowa tablice dlugosci n
	for i in range(n):
		tmp[i][0] = i								# tmp[i] zawiera indeks odpowiadjacy i-temu przedmiotowi w A
		tmp[i][1] = (A[i][0]/A[i][1])		 		# oraz jego cene jednostkowa
	tmp.sort(key = lambda tup: tup[1])				# sortujemy po cenie jednostkowej
	for i in range(n-1, -1, -1):
		if k == 0:
			return profit
		if k >= A[tmp[i][0]][1]:
			profit += A[tmp[i][0]][0]
			k -= A[tmp[i][0]][1]
		else:
			profit += k*tmp[i][1]
			k = 0


print( knapsack( [ (1,1), (10,2), (6,3) ], 3 ))


