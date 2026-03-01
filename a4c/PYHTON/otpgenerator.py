import random
import time
file_1 = open("store passwords.txt","a+")
while True :
    a = random.randint(100001,999999)
    reply_1 = input('Do you want to generate a unique password -->>')
    if reply_1 == 'yes' :
        file_1.write(str(a))
        time.sleep(1)
        print("Here is your unique password --->",a)
    elif reply_1 == 'YES' :
         file_1.write(str(a))
         time.sleep(1)
         print("Here is your unique password --->",a)
    elif reply_1 == 'NO':
        print('have a good day')
        file_1.close
        time.sleep(2)
        break
    reply_2 =input('Do you want to create more unique passwords -->')
    b = random.randint(100001,999999)
   
    if reply_2 == 'yes' :
         time.sleep(1)
         file_1.write(str(b))
         print("Here is your unique password --->",b)
    elif reply_2 == 'YES' :
         time.sleep(1)
         file_1.write(str(b))
         print("Here is your unique password --->",b)
    elif reply_2 == 'NO':
        print('have a good day')
        file_1.close
        time.sleep(2)
        break

