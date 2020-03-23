def partition3(a, l, r):
   x, j, t = a[l], l, r
   i = j
   while i <= t :
      if a[i] < x:
         a[j], a[i] = a[i], a[j]
         j += 1

      elif a[i] > x:
         a[t], a[i] = a[i], a[t]
         t -= 1
         i -= 1
      i += 1
   return j, t

def quicksort3arr(arr, l ,r):
    if l >= r: return
    i,j = partition3(arr, l, r)

    quicksort3arr(arr, l, i-1)
    quicksort3arr(arr, j+1, r)


arr = [1,45,7,4,867,233,78,93,46,9,2,55,797,9,243,4656,7,78,66,8]
quicksort3arr(arr,0,len(arr)-1)
print(arr)