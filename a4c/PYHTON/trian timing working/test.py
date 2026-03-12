f=open("metro_stations_csv.txt","r")
a=f.readlines()

for i in range(len(a)): 
    a[i]=a[i].split(",")
for i in range(len(a)):
    print(a[i][1])
