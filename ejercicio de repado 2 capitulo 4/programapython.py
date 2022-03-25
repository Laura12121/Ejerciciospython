n_1=int(input("ingrese el primer numero:  "))
n_2=int(input("ingrese el segundo numero:  "))
n_3=int(input("ingrese el tercer numero:   "))

if n_1 <= n_2 and n_1 <= n_3:
    menor=(n_1)
elif n_2 <=n_1 and n_2<= n_3: 
    menor=(n_2)
else:
    menor=(n_3)
print(f"el numero menor es {menor} ")
