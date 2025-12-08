for i in range(1,7):
    for j in range(i,7):
        print('-',end='')
    
    print("$"*(i*2-1))
    
for i in range(7,0,-1):
    for j in range(7,i,-1):
        print('-',end='')
    
    print("$"*(i*2-1))