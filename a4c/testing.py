n=int (input("Enter the limit :"))
a=-1
b=1
for i in range (0,n+1):
    c=a+b
    print (c, end=' ')
    a=b
    b=c