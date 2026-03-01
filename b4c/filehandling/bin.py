import pickle
def lmao():
        f=open("fuckyou.bin",'wb')
        a=0
        while a!=1 :
            b=input("name:->")
            c=int(input("age-->"))
            if b=="ff":
                break
            d=[b,c]
            
            pickle.dump(d,f)
            
        f.close()

def lol():
    try:
            f= open("fuckyou.bin",'rb')
            while True:
                    a=pickle.load(f)
                    for i in a :
                        print(i)

    except:
        print("error openinig file")

a=input("?")
if a =="1":
       lmao()
else:
      lol()

            
