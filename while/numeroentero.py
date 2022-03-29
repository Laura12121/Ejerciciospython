n=int(input("digite su numero:  "))
x=1
acumulador=1
for i in range(1,n+1):
    x1=(x*i)**2
    acumulador=acumulador*x1
print(acumulador)