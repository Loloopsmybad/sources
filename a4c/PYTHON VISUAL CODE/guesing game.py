import random
import time
a = random.randint(0,100)
print("YOU HAVE TO GUESS WHAT NUMBER I AM THINK OF OK? ")
time.sleep(2)
print('wait let me think of a number ')
time.sleep(3)
print("ok i've guessed it , now you have to guess wht number it is")
print("here's a hint -->>")
if a >= 1 and a <= 20 :
  print("the number's between 1 to 20 OR it can be 1 or 20 or even 10 ")
elif a >= 20 and a <= 40 :
  print("the number is between 20 to 40 OR it can even be 10 or 40 or even 40 ")
elif a >= 40 and a <= 60 :
  print("the number is between 40 to 60 OR it can even be 40 or 60 or even 50")
elif a >= 60 and a <= 80 :
  print("the number is between 60 to 80 OR it can even be 60 or  8 or even 70")
elif a >= 80 and a<= 100 :
 print("the number is between 80 to 100 OR it can even be 80 or 100 or even 90 ")


while True:
     gg=int(input('GUESS WHAT NUMBER AM I THINING -->>'))


     if gg == a :

       print("that's correct !!!! ")
       time.sleep(6)
       break  
     elif gg >=a :
       
       print('too high!!!')
     elif gg <= a :
         print('too low !!!')
         