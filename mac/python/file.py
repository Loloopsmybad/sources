with open("data.txt","r") as file:
    f=file.readlines()
    print(f)
for i in range(len(f)):
    a=f[i].strip().split()
    for j in range(len(a)) : 
            a[j]=int(a[j])**2
            print(a[j])
            a[j]=str(a[j])
    b=''
    for j in a :
       b=b+j+' '
    f[i]=b+'\n'

with open("nigger.txt","w") as file2:
     file2.writelines(f)
print(f)


    