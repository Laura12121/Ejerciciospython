X=7
Y=8
Caballo_x= 0
Caballo_y= 0
print(f"({Caballo_x}, {Caballo_y})", end="  ")
flow= True  
while Caballo_x !=X and Caballo_y !=Y: 
    if flow: 
        Caballo_x += 1
        Caballo_y += 2
    else:
        Caballo_x +=2
        Caballo_y +=1
    print(f"({Caballo_x},  {Caballo_y})", end=" ")
    flow= not flow

