# Program to write and read employee records in a binary file
import pickle
'''
print("WORKING WITH BINARY FILES")
bfile=open("empfile.dat","wb")
recno=1
print ("Enter Records of Employees")
print()
#taking data from user and dumping in the file as list object
while True:
 print("RECORD No.", recno)
 eno=int(input("\tEmployee number : "))
 ename=input("\tEmployee Name : ")
 ebasic=int(input("\tBasic Salary : "))
 allow=int(input("\tAllowances : "))
 totsal=ebasic+allow
 print("\tTOTAL SALARY : ", totsal)
 edata=[eno,ename,ebasic,allow,totsal]
 pickle.dump(edata,bfile)
 ans=input("Do you wish to enter more records (y/n)? ")
 recno=recno+1
 if ans.lower()=='n':
    print("Record entry OVER ")
    print()
    break
# retrieving the size of file
print("Size of binary file (in bytes):",bfile.tell())
bfile.close()
# Reading the employee records from the file using load() module
print("Now reading the employee records from the file")
print()
readrec=1
try:
  with open("empfile.dat","rb") as bfile:
    while True:
      edata=pickle.load(bfile)
      print("Record Number : ",readrec)
      print(edata)
      readrec=readrec+1
except EOFError:
 pass
bfile.close()

'''


import pickle
def lol():
  f = open ("kill.bin",'wb')
  
  d= 1
  while d==1:
    b = input ("enter ")
    
    l = input ("enter ")
    
    c=[b,l] 
    pickle.dump(c,f)   
    if b=='a':
      d=0


  f.close()
  

#lol()



def pp():

    try:  
      k= open("die.dat","ab")
      f = open ("kill.bin","rb")
      while True:
        op = pickle.load(f)
        
        if op[1]=='lol':
          op[1]='upieceoftrash'
        pickle.dump(op,k)
        print(op)

    except EOFError:
            pass
    k.close()
    f.close()
pp()



import pickle
def loll():
      print("stfun")
      
      with open("die.dat","rb") as bfile:
        while True:
         try:
             
          edata=pickle.load(bfile)
          print("Record Number : ")
          print(edata)
         except:
            break
      bfile.close()

loll()

import pickle
def SHOWINFO():
 
 f=open("die.dat","rb")
 while True:
    try:
      g=pickle.load(f)
      print(g)
    except:
      break
    f.close()

#SHOWINFO()


'''
import pickle

for i in range (3):
  with open("kill.bin",'ab') as f :
    a= input("name")
    b= input("type")
    s=[a,b]
    pickle.dump(s,f)
    f.close()

'''  