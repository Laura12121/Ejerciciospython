papel=4
tijera=2
piedra=3

p_1=int(input("digite puntaje de persona 1: "))
p_2=int(input("digite puntaje de persona 2:  "))
if p_1== papel and p_2==piedra:
    print("papel envuelve a piedra")
elif p_1==papel and p_2==papel:
    print("empate entre papel")
elif p_1==papel and p_2==tijera:
    print("tijera corta papel")
elif p_1==tijera and p_2==tijera:
    print("empate entre tijera")
elif p_1==tijera and p_2==papel:
    print("tijera corta papel")
elif p_1==tijera and p_2==piedra: 
    print("piedra mata a tijera")
elif p_1==piedra and p_2==piedra:
    print("empate entre piedras")
elif p_1==piedra and p_2==papel:
    print("papel envuelve a piedra")
elif p_1==piedra and p_2==tijera:
    print("piedra le gana a tijera")