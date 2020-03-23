def counting_sort(arr):			# dla <0;max>
	n = len(arr)
	k = max(arr) + 1
	output = [0] * n
	count = [0] * k
	for i in range(n): # count
		count[arr[i]] += 1
	for i in range(k): # cumulative sum
		count[i] += count[i - 1]
	for i in range(n-1, -1, -1): # place elements in output
		output[count[arr[i]]-2] = arr[i]
		count[arr[i]] -= 1
	return output


arr = [22, 4, 21, 2, 1, 35, 8, 6, 3, 3, 5, 1, 2, 2, 4, 4, 7, 8, 8, 5, 3, 1, 12]
new_arr = counting_sort(arr)
print(new_arr)