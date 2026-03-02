import math
a=int(input("enter the start of range: "))
b=int(input("enter the end of range: "))
l=[]
for i in range (a,b+1):
    if i<=b:
        l.append(i)

import random
ran=random.choice(l)
print(ran)
while True:
    guess=int(input("Enter the guess of the number: "))
    if guess>ran:
        if guess==(ran-):
            print("Super close")
        elif guess>(ran-5):
            print("you are close go lower")
        else:
            print("you are close a bit lower")
    if guess<ran:
        if guess==(ran+1):
            print("Super close")
        elif guess<(ran+5):
            print("you are close go higher")
        else :
            print("you are close a bit higher")
    if guess==ran:
        print("congrats, you WON!!!")
        break


























"""

    if c>ran:
        if c<=(ran-10):
            print(c,"you are close make it higher")
        elif c<=(ran-5):
            print(c,"you are super close just a little bit higher")
        else:
            print(c,"is low try again")
    elif c==ran:
        print(c,"congrats, you guessed right, you took,",d,"try")
        break
    elif c<ran:
        if c>=(ran+5):
            print(c,"you are super close just a little bit lower")
        elif c>=(ran+10:
            print(c,"you are close make it lower")
        else:
            print(c, " is high, try again")
    d+=1
"""
