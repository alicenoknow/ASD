
def algEukl(a,b):
    while(b):
        c=a%b
        a=b
        b=c
    return a

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))

print("NWD(",a,",",b,"): ", algEukl(a,b))