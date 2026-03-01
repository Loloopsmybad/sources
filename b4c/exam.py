'''import csv
file=open("teacher.csv","w")
writer=csv.writer(file)
writer.writerow(["t_id","teacher name","desg"])
a=0
b=[]
while a!=1:
    k=input("t_id")
    b.append(k)
    h=input("teacher name")
    b.append(h)
    f=input("desg")
    b.append(f)
    x=input("do you want to continue?")
    if x=="no":
        a=a+1
        writer.writerows(b)
        b.clear()
        
    else:
        a=0
file.close()


'''







import csv
file=open("teacher.csv","r")
reader=csv.reader(file)
a=[]
for row in reader:
    k=str(row[2])
    if k=='god':
       print("okie")
file.close()
     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
'''

import csv 

f= open("people.csv","r")
reader=csv.reader(f)
a=reader
print(a)
for row in reader:
    print(row)
f.close()

'''














'''
import csv
f=open("teacher.csv","w")
writer=csv.writer(f)
writer.writerow(["t_id","teacher name","desg"])
a=0
b=[]
while a!=1:
    k=input("t_id")
    b.append(k)
    h=input("teacher name")
    b.append(k)
    f=input("desg")
    b.append(k)
    x=input("do you want to continue?")
    if x=="no":
        a=a+1
        writer.writerows(b)
        b.clear()
        
    else:
        a=0
f.close()'''
    