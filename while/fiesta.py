ingreso=str(input("desea ingresar?:  "))
ch=0
cm=0
pro_h=0
pro_m=0
acu_h=0
acu_m=0
e_min=0

if ingreso=="si" or ingreso=="si" or ingreso=="si": 
    
    while ingreso=="si" or ingreso=="si" or ingreso=="si": 
        print("\nNuevo usuario")
        edad=int(input("que edad tiene: "))
        t_h_m=ch+cm

        if edad>=18:
            nombre=str(input("nombre completo:  "))
            genero=str(input("genero:  "))
        
            if e_min<edad and edad !=0:
                ed=edad
            
                if  genero=="hombre":
                    ch +=1
                    acu_h=acu_h+edad
                    pro_h=int(acu_h/ch)
        if  genero=="mujer" : 
                cm +=1
                acu_m=acu_m+edad
                pro_m=int(acu_m/cm)
        elif edad>0 and edad<18:
            print("no puede ingresar,no tiene la edad requerida para el ingreso")
        else:
            break
    print(f"""\nTotal asistentes a la fiesta: {t_h_m}\nTotal asistentes hombres: {ch}.\nTotal mujeres: {cm}
            \nPromedio edad hombre: {pro_h}\nPromedio edad mujeres: {pro_m}
            \nEdad minima de personas que asistieron: {ed}""")
else:
    print("salir de pagina")