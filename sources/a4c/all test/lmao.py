'''

a= int(input("nu"))
x=1
p=1
while x<=a:

    p=p*x
    x+=1

print(p)
'''


for i in range (5):
    for k in range (0,i):
        print ("  ", end="")
    for j in range (5-i,0,-1):
        print (j, end=" ")
    print()