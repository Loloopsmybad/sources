n = int (input ("enter a number -->")) # type: ignore
k=1
d=0
for i in range (1,n+1):
        for j in range (1,i+1):
            k = k*j 
        d = d+k
        k=1
print("sum of factorial in series is-->",d)

            
for i in range (1,10):
    print("sum of value ---> ")

