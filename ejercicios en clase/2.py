evaluacion_f=float(input("ingrese la nota del examen:  "))
quiz1=float(input("ingrese la nota final:   "))
quiz2=float(input("ingrese la nota final:    "))
quiz3=float(input("ingrese la nota final:   "))
trabajo_final=float(input("digite nota de los quiz:  "))
nota_final=((evaluacion_f*0.50)+(((quiz1+quiz2+quiz3)/3)*0.20)+(trabajo_final)*0.30)
print(f'la nota final del estudian  es:  {nota_final:  .2f}  ')