import mysql.connector

mydb =mysql.connector.connect(host="localhost", user="root",password="csip")
cursor= mydb.cursor()
cursor.execute("use bookmanagement")

def available_books():
    print("")
    a= int(input("enter the serial number -->"))
    print("")
    b=input(" book_name -->")
    print("")
    c= input("genre -->")
    print("")
    d= input(" quantity -->")
    print("")
    e= input(" author -->")
    print("")
    f= input(" publication -->")
    print("")
    g= int(input(" price -->"))
    print("")
    str= "insert into cms (Sr_No,book_name,genre,quantity,author,publication,price) values(%s,%s,%s,%s,%s,%s,%s)"
    values=(a,b,c,d,e,f,g)
    print("record added successfully !!")
    cursor.execute(str,values)
    mydb.commit()

def readavailable_books():
    a= int(input("enter the book_name -->"))
    print("")
    str= ("select * from available_books where book_name= %s")
    cursor.execute(str,(a,))
    myresult=cursor.fetchall()
    for x in myresult:
        print(x)



def sell_rec():
    a= input("enter the Customer number -->")
    print("")
    b=int(input(" PHONE_NUMBER -->"))
    print("")
    c= input(" the BOOK_NAME -->")
    print("")
    d=int(input("quantity -->"))
    print("")
    e= int(input("price -->"))
    print("")
    

    str= "insert into crd (Customer,PHONE_NUMBER,BOOK_NAME,quantity,price) values(%s,%s,%s,%s,%s)"
    values=(a,b,c,d,e)
    print("record added successfully !!")
    cursor.execute(str,values)
    mydb.commit()

def readsell_rec():
    a= int(input("enter the Customer name -->"))
    str= ("select * from sell_rec where Customer= %s")
    cursor.execute(str,(a,))
    myresult=cursor.fetchall()
    for x in myresult:
        print(x)




print("welcome to the case mangement progrgram !!")
k= 1
while k!=0:
      print("-->do you want to enter a record? type --> 'write'")
      print("")
      print("-->or do you want to read record ?type --> 'read'")
      print("")
      print("-->read or write ") 
      print("")
      print ("-->enter no to exit")
      print("")
      s = input("-->enter your choice ")
      print("")
      if s.lower()=="no":
                    k=0
                    break
      elif s.lower() =="write":
                    print("-->which record do you want to enter ?")
                    print("")
                    print("1) new book entry ")
                    print("")
                    print("2) new book customer details")
                    print("")
                  
                    t=int(input("choice ?"))
                    if t == 1:
                        available_books()
                    elif t == 2:
                        sell_rec()
                    else:
                        print("-->invalid input please choose from 1,2")

      elif s.lower() =="read":
                    print("-->which record do you want to read ?")
                    print("")
                    print("1) book entry ")
                    print("")
                    print("2) customer details")
                    print("")

                    t=int(input("choice ?"))
                    if t == 1:
                        readavailable_books()
                    elif t == 2:
                        readsell_rec()
                    else:
                        print("-->invalid input please choose from 1,2")
