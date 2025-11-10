k= input ("enter something ")
p= ''
v = ['a','e','i','o','u']
for i in range(len(k)): 
    if k[i] in v:
        p=p+(k[i].replace(k[i],"*"))
        
    else:
        p=p+(k[i])
print(p)