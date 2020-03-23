def bucket_sort_garek(arr,k):
    buckets = [[] for _ in range(k)]
    for i in arr: buckets[int(k*i)].append(i)
    for i in range(k): buckets[i].sort()
    res = []
    for i in range(k): res.extend(buckets[i])
    return res


arr = [0.2, 0.12, 0.56, 0.78, 0.12, 0.25, 0.67, 0.9, 0.54, 0.67]
res = bucket_sort_garek(arr, 10)
print(res)