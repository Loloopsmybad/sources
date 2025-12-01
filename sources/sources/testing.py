import csv


f = open ('data.csv','r')
f1 = open ('data.csv','a')
r=csv.reader(f)
w=csv.writer(f1)

for row in r :
 
    if row[2]=='CS':
        a='k'
        row[2]=a
        w.writerow(row[2])
    print(row)
f1.close()   
f.close()
