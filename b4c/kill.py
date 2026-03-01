import pickle
def loll():
    try:
      with open("kill.bin","rb+") as f:
        while True:
          print("hi")
          edata=pickle.load(f)
          print("Record Number : ")
          for i in edata :
            print(i)
          
    except EOFError:
     pass
    f.close()
loll()