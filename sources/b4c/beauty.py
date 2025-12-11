import random
import time
c= 20 
gap=0
d=0
d1=0
while True:
    a = random.randint(1,99)
    b= random.randint(1,99)
    if d ==0:
        for i in range(c):
            print(end=" ")
        c= c-4
    elif d==1:
        c=c+4
        for i in range(c):
            print(end=" ")
    print(a,end=" ")
    
        
    print(b)
    if gap==20:
        d1=1
    elif gap==0:
        d1=0
    if c==0:
        d=1
    elif c== 20 :
        d=0
    time.sleep(0.1)