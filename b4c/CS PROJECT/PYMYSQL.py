import mysql.connector

mydb =mysql.connector.connect(host="localhost", user="root",password="csip")
cursor= mydb.cursor()
cursor.execute("use cms")

def case_details():
    print("")
    a= int(input("enter the case number -->"))
    print("")
    b=input(" Case_Name_CLAIMANT_VS_RESPONDENT -->")
    print("")
    c= input("Date_of_filing -->")
    print("")
    str= "insert into cms (Case_No,Case_Name_CLAIMANT_VS_RESPONDENT,Date_of_filing) values(%s,%s,%s)"
    values=(a,b,c)
    print("record added successfully !!")
    cursor.execute(str,values)
    mydb.commit()

def readcase_details():
    a= int(input("enter the case number -->"))
    print("")
    str= ("select * from cms where Case_No= %s")
    cursor.execute(str,(a,))
    myresult=cursor.fetchall()
    for x in myresult:
        print(x)


def counsel_details():
    a= int(input("enter the case number -->"))
    print("")
    b=input(" Counsel of (respondent or claimant) -->")
    print("")
    c= input("name of the counsel-->")
    d= int(input("enter the phone number of counsel-->"))
    print("")
    e= input("enter the email id of the counsel-->")

    str= "insert into con (Case_No,Counsel_of,Date_of_filing,Name,PhoneNO,EmailID) values(%s,%s,%s,%s,%s)"
    values=(a,b,c,d,e)
    print("record added successfully !!")
    cursor.execute(str,values)
    mydb.commit()

def readcounsel_details():
    a= int(input("enter the case number -->"))
    print("")
    str= ("select * from con where Case_No= %s")
    cursor.execute(str,(a,))
    myresult=cursor.fetchall()
    for x in myresult:
        print(x)

def calimant_respondent_details():
    a= int(input("enter the case number -->"))
    print("")
    b=input(" Category (claimant/respondent) -->")
    print("")
    c= input("name of the claimant/respondent -->")
    print("")
    d=input("address of the respondent/claimant -->")
    print("")
    e= int(input("enter the phone number of counsel-->"))
    print("")
    f= input("enter the email id of the counsel-->")
    print("")

    str= "insert into crd (Case_No,Category,Name,Address,PhoneNO,EmailID) values(%s,%s,%s,%s,%s,%s)"
    values=(a,b,c,d,e,f)
    print("record added successfully !!")
    cursor.execute(str,values)
    mydb.commit()

def readcalimant_respondent_details():
    a= int(input("enter the case number -->"))
    str= ("select * from crd where Case_No= %s")
    cursor.execute(str,(a,))
    myresult=cursor.fetchall()
    for x in myresult:
        print(x)

def court_details():
    a= int(input("enter the case number -->"))
    print("")
    b=input(" Case_Name_CLAIMANT_VS_RESPONDENT -->")
    print("")
    c=input(" Judge name -->")
    print("")
    d= input("next date of hearing -->")
    print("")
    str= "insert into ctd (Case_No,Court,JudgeName,Next_Date_Of_Hearing) values(%s,%s,%s,%s)"
    values=(a,b,c,d)
    print("record added successfully !!")
    cursor.execute(str,values)
    mydb.commit()

def readcourt_details():
    a= int(input("enter the case number -->"))
    print("")
    str= ("select * from ctd where Case_No= %s")
    cursor.execute(str,(a,))
    myresult=cursor.fetchall()
    for x in myresult:
        print(x)

def stage_details():
    a= int(input("enter the case number -->"))
    print("")
    b=input(" Case_Name_CLAIMANT_VS_RESPONDENT -->")
    print("")
    print("1. PRELIMINARY HEARING 2. COMPLETION OF PLEADINGS 3. AFFIDAVIT OF ADMISSION AND DENIAL 4.CROSS EXAMINATION 5. AWARD RESERVED 6. AWARD PRONUONCED")
    c= input("stage of hearing-->")
    print("")
    str= "insert into stg (Case_No,Case_Name_CLAIMANT_VS_RESPONDENT,Stage_Of_Hearing) values(%s,%s,%s)"
    values=(a,b,c)
    print("record added successfully !!")
    cursor.execute(str,values)
    mydb.commit()

def readstage_details():
    a= int(input("enter the case number -->"))
    print("")
    str= ("select * from stg where Case_No= %s")
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
                    print("1) case details ")
                    print("")
                    print("2) counsel details")
                    print("")
                    print("3) claiment or respondent details")
                    print("")
                    print("4)  court details details")
                    print("")
                    print("5) case stage details")
                    print("")
                    t=int(input("choice ?"))
                    if t == 1:
                        case_details()
                    elif t == 2:
                        counsel_details()
                    elif t==3:
                        calimant_respondent_details()
                    elif t==4:
                        court_details()
                    elif t== 5:
                        stage_details()
                    else:
                        print("-->invalid input please choose from 1,2,3,4,5")

      elif s.lower() =="read":
                    print("-->which record do you want to read ?")
                    print("")
                    print("1) case details ")
                    print("")
                    print("2) counsel details")
                    print("")
                    print("3) claiment or respondent details")
                    print("")
                    print("4)  court details details")
                    print("")
                    print("5) case stage details")
                    print("")
                    t=int(input("choice ?"))
                    if t == 1:
                        readcase_details()
                    elif t == 2:
                        readcounsel_details()
                    elif t==3:
                        readcalimant_respondent_details()
                    elif t==4:
                        readcourt_details()
                    elif t== 5:
                        readstage_details()
                    else:
                        print("-->invalid input please choose from 1,2,3,4,5")
