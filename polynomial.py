
def polynomial(r):
    res = 0
    x=int(input("Variable x: "))
    for i in range (r-1,-1,-1):
        print("Coefficient x^",i,": ",end ="")
        a=int(input())
        res += x**i * a
    return res

r = int(input("Degree: "))
print("Result: ", polynomial(r))
