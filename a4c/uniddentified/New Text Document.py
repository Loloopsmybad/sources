k = input("")
c=k
a=0
b=0
for i in range(len(k)):
    if c[i].isupper == True:
        a=a+1
        print(a,"TRUE") 
    elif c[i].islower == True:
        b=b+1
        
        print(b) 