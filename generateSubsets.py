
def genereteSubsets(n,p,t):
    if n==p:
        for i in range (0,n):
            if t[i]==1:
                print(i, end="")
        print("")
    else:
        t[p] = 0
        genereteSubsets(n,p+1,t)
        t[p] = 1
        genereteSubsets(n,p+1,t)



t = [0,0,0,0,0]
n = 5

genereteSubsets(n,0,t)
