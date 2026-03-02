import random
import math
import sys
import time
t=[]
name=input("Enter your name :")
time.sleep(1)
print("                                                                                        \
        THIS IS A NUMBER 21 GAME , the rules are as follows; \n"
       "1.) The first one to come to number 21 or greater WINS the game. \n"
       "2.) So",name," you have to choose from 1 to 3 only rest is automated. \n"
       "3.) If you choose a number more than 3 the game will crash and you have to restart ")
print("                                                                                                                         ")
time.sleep(3)
start=int(input("Press 1 for first chance 'OR' 2 for second chance :"))
def second() :
    print("                                                                          \
                          --- THE GAME STARTS--                        \
                                                                                      ")
    
    print(" ***** Computer is thinking***  ")
    time.sleep(3)
    i=random.choice('123')
    i=int(i)
    print("The number is :",i)
    t.append(i)



    
def first():
    print("                                                                          \
                          --- THE GAME STARTS--                        \
                                                                                      ")
    i=int(input("choose any one from '1,2,3' :"))
    print("The number is :",i)
    print("                                                                                                                         ")
    print(" ***** Computer is thinking***  ")
    time.sleep(3)
    j=random.choice('123')
    i=int(i)
    j=int(j)
    r=i+j
    print("The number is :",r)
    t.append(r)
    print("                                                                                                                         ")
    
def char():
    print("                                                                                                                         ")
    j=int(input("choose any one from '1,2,3' :"))
    if j<4:
        w=t[0]
        k=w+j
        k=int(k)
        print("the number is",k)
        print("                                                                                                                         ")
        t.clear()
        t.append(k)
        if k>=21 or w>=21:
            print("Congratulations",name," you WON the game")
            sys.exit()
    elif j>=4:
        print("You had to choose till 3 and you chose",j,"Please restart the game")
        sys.exit()
    com()
def com():
    c=random.choice('123')
    c=int(c)
    w=t[0]
    u=w+c
    u=int(u)
    print(" ***** Computer is thinking***  ")
    time.sleep(3)
    print("the number is",u)
    t.clear()
    t.append(u)
    if u>=21 or w>=21:
        print("Sorry, ",name,"you LOST try again")
        sys.exit()
    char()   
if start==1:
     first()
     char()
if start==2:    
    second()
    char()
