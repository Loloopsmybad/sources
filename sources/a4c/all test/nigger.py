def cou(at):
    a=0
    cc=0
    for i in range(len(at)):
        if at[i]==0:
            if cc>=a:
                a=cc 
            cc=0    
            
        elif at[i]==1:
            cc+=1
            
    print(a)
    
    
    
cou([1,1,1,1,0,0,0,0,0,1,0,1,1,0,0])