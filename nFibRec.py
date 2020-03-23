def nFibRec(n,a = 0,b = 1):
        if n==1:
            return b
        return nFibRec(n-1,b,a+b)


print(nFibRec(88))