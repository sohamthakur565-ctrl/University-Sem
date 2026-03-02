#SOURCE CODE FOR LIBRARY MANAGEMENT
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='root')
mycursor=mydb.cursor()
print("""
━━━━━━━━━━━━━━━━━━━━━━━

Welcome To Library Management System

━━━━━━━━━━━━━━━━━━━━━━━
""")
#Creating Database
mycursor.execute("create database if not exists library_3")
mycursor.execute("use library_3")
mycursor.execute("create table if not exists available_books(id int, name varchar(25), subject varchar(25), quantity int)")
mycursor.execute("create table if not exists issued(id int, name varchar(25),subject varchar(25), s_name varchar(25), s_class varchar(25))")
mycursor.execute("create table if not exists login(user varchar(25), password varchar(25))")
mydb.commit()
#Entering data
flag=0
mycursor.execute("select * from login")
for i in mycursor:#0
    flag=1
if flag==0:
    mycursor.execute("insert into login values('user','ng')")
    mydb.commit()
#Loops///Main Working

while True:
    print("""
1.Login
2.Exit
""")
    ch=int(input("Enter your choice:"))
    if ch==1:
        pas=input("Enter password:")
        mycursor.execute("select * from login")
        for i in mycursor:#var1,var2=(x,y)
            t_user,t_pas=i
        if pas==t_pas:
            print("Login Successfully...")
            loop1='n'
            while loop1=='n':
                print("""
━━━━━━━━━━━━━━━━━━━
1.Add New Books
2.Remove Any Book
3.Issue Book To Student
4.Return Book
5.View Available Books
6.View Issued Books
7.Logout
━━━━━━━━━━━━━━━━━━━
""")
                ch=int(input("Enter your choice:"))
                if ch==1:
                    loop2='y'
                    while loop2=='y':
                        print("All information are mandatory to be filled!!")
                        idd=int(input("Enter book id (numbers only):"))
                        name=input("Enter book name:")
                        subject=input("Enter subject:")
                        quan=int(input("Enter quantity:"))
                        mycursor.execute("insert into available_books values('"+str(idd)+"','"+name+"','"+subject+"','"+str(quan)+"')")
                        mydb.commit()
                        print("Data Inserted Successfully...")
                        loop2=input("Do you want to add another book?(y/n)").lower()
                    loop1=input("Do you want to logout? (y/n)").lower()
                elif ch==2:
                    idd=int(input("Enter Id to remove book:"))
                    mycursor.execute("select * from available_books")
                    flag=0
                    for i in mycursor:
                        t_id,t_name,t_subject,t_quan=i
                        if t_id==idd:
                            flag=1
                    if flag==1:
                        mycursor.execute("delete from available_books where id='"+str(idd)+"'")
                        mydb.commit()
                        print("Data Successfully Deleted...")
                    else:
                        print("Wrong Input...")               
                elif ch==3:
                    loop2='y'
                    while loop2=='y':

                        idd=int(input("Enter Book ID:"))
                        s_name=input("Enter Student Name:")
                        s_class=input("Enter Student Class:")
                        mycursor.execute("select*from available_books where id='"+str(idd)+"'")

                        flag=0
                        for i in mycursor:
                            t_id,t_name,t_subject,t_quan=i
                            flag=1
                        quan=t_quan-1
                        if flag==1:
                            if t_quan>=0:
                                mycursor.execute("insert into issued values('"+str(idd)+"','"+t_name+"','"+t_subject+"','"+s_name+"','"+s_class+"')")
                                mycursor.execute("update available_books set quantity='"+str(quan)+"'")
                                mydb.commit()
                                print("Successfully issued")
                                loop2=input("Do yo want to issue more books? (y/n)").lower()
                        
                            else:
                                print("Book not available...")
                        else:
                            print("Invalid Input...")
                    loop1=input("Do you want to log out?(y/n)").lower()                      
                    
                elif ch==4:
                    loop2='y'
                    while loop2=='y':
                        idd=int(input("Enter book id:"))
                        s_name=input("Enter student name:")
                        s_class=input("Enter student class:")
                        mycursor.execute("select * from issued")
                        flag=0
                        for i in mycursor:
                            t_id,t_name,t_subject,t_s_name,t_s_class=i
                            if t_id==idd and t_s_name==s_name and t_s_class==s_class:
                                flag=1
                            if flag==1:
                                mycursor.execute("select * from available_books where id='"+str(idd)+"'")
                                for i in mycursor:
                                    t_id,t_name,t_subject,t_quan=i
                                quan=t_quan+1
                                mycursor.execute("delete from issued where id='"+str(idd)+"'and s_name='"+s_name+"'and s_class='"+s_class+"'")
                                mycursor.execute("update available_books set quantity='"+str(quan)+"'")
                                mydb.commit()
                                print("Successfully Issued...")
                                loop2=input("Do you want to issue more book?(y/n)").lower()
                            else:
                                print("not issued yet...")
                            loop1=input("Do you want to logout?(y/n)").lower()
                elif ch==5:
                    mycursor.execute("select * from available_books")
                    print("ID | NAME | SUBJECT | QUANTITY")
                    for i in mycursor:
                        a,b,c,d=i
                        print(f"{a}|{b}|{c}|{d}")
                elif ch==6:
                    mycursor.execute("select * from issued")
                    print("ID | NAME | SUBJECT | S_NAME | S_CLASS")
                    for i in mycursor:
                        a2,b2,c2,d2,e2=i
                        print(f"{a2}|{b2}|{c2}|{d2}|{e2}")
                elif ch==7:
                    break
        else:
            print("Wrong Password...")
    elif ch==2:
        break
