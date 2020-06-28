def fib_dynamic(n):
    fib = [0]*(n+1)
    fib[0] = 0
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]


def fib_dynamic2(n):
    if n <= 1:
        return 1
    fib1 = 1
    fib2 = 1
    for i in range(2, n+1):
        fib = fib1 + fib2
        fib2 = fib1
        fib1 = fib
    return fib


def fib_dynamic3_mem(n, fib):   # fib = [0]*(n+1)
    if fib[n] > 0:
        return fib[n]
    fib[n] = fib_dynamic3_mem(n-1, fib) + fib_dynamic3_mem(n-2, fib)
    return fib[n]


print(fib_dynamic(6))
