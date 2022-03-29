contar=0
texto1=input("digite:  ")
alfabeto="AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
for i in texto1:   
    if i in alfabeto: 
        contar+=1
    
    
    else:
        print("se encontraron caracteres no alfabeticos")
        break 


if contar==len(texto1):
    print("se encontraron que todos los caracteres son alfabeticos")