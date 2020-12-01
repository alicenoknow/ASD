import time

def factorial_recursive(n):
  if n == 0 or n == 1:
    return 1
  else:
     return n*factorial_recursive(n-1)


def factorial_dp(n):
    f = [0 for _ in range(n+1)]
    f[0] = 1
    for i in range(1,n+1):
        f[i] = i * f[i - 1]
    return f[n]


def factorial_prime(n):
    prime = [True] * (n + 1)
    result = 1
    for i in range(2, n + 1):
        if prime[i]:
            j = i + i
            while j <= n:
                prime[j] = False
                j += i
            sum = 0
            t = i
            while t <= n:
                sum += n // t
                t *= i
            result *= i ** sum
    return result


start_time = time.time()
#print(factorial_dp(7000))
print(factorial_prime(7000))
print("--- %s seconds ---" % (time.time() - start_time))