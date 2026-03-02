'''#Q1.
name=input("Enter your name :")
maths=int(input("Enter your Maths marks :"))
english=int(input("Enter your English marks :"))
physics=int(input("Enter your Physics marks :"))
chemistry=int(input("Enter your Chemistry marks :"))
cs=int(input("Enter your Computer Science marks :"))
avg=(maths+english+physics+chemistry+cs)/5
print(avg);
if avg<=50:
    grade='E'
elif avg<=60:
    grade='D'
elif avg<=70:
    grade='C'
elif avg<=80:
    grade='B'
elif avg<=90:
    grade='A'
elif avg>90:
    grade="A+"
print(name,"your average marks are:",avg,"and you grades are",grade)

#Q2.
cost=int(input("Enter the cost of the product :"))
discount=int(input("Enter the discount percentage in numbers :"))
d=discount/100
d=1-d
cp=cost*d
print("The selling price after applying discount of",discount,"% on",cost,"is",cp)



#Q3.
shape=input("Enter the name of the shape :")
def triangle():
    n=input("What do you want to find of triangle 'Area or Perimeter' :")
    if n=='Area' or 'area':
        height=int(input("enter the a height of the Triangle (in cm) :"))
        base=int(input("enter the a base of the Triangle (in cm) :"))
        area=0.5*height*base
        print("The area of the triangle is :",area)
    elif n=='Perimeter' or 'perimeter':
        side=int(input("enter the a side of the Triangle (in cm) :"))
        perimeter=side*3
        print("The perimeter of the triangle is :",perimeter)

def circle():
    n=input("What do you want to find of triangle 'Area or Circumfrence' :")
    if n=='Area' or 'area':
        radius=int(input("Enter the radius of the circle (in cm) :"))
        area=3.14*radius**2
        print("The area of the circle is :",area)
    elif n=='Circumfrence or circumfrence':
        radius=int(input("Enter the radius of the circle (in cm) :"))
        c=2*3.14*radius
        print("The circumfrence of the circle is :",c)
def rec():
    n=input("What do you want to find of rectangle 'Area or Perimeter' :")
    if n=='Area' or 'area':
        lenght=int(input("enter the a lenght of the Rectangle (in cm) :"))
        width=int(input("enter the a width of the Rectangle (in cm) :"))
        area=lenght*width
        print("The area of the Rectangle is :",area)
    elif n=='Perimeter' or 'perimeter':
        lenght=int(input("enter the a lenght of the Rectangle (in cm) :"))
        width=int(input("enter the a width of the Rectangle (in cm) :"))
        perimeter=2*(lenght+width)
        print("The area of the triangle is :",perimeter)
def square():
    n=input("What do you want to find of square 'Area or Perimeter' :")
    if n=='Area' or 'area':
        side=int(input("Enter the side of the square (in cm) :"))
        area=side*side
        print("The area of the square is :",area)
    elif n=='Perimeter' or 'perimeter':
        side=int(input("enter the a side of the square (in cm) :"))
        perimeter=side*4
        print("The perimeter of the square is :",perimeter)
if shape =='triangle' or 'Triangle':
    triangle()
elif shape =='Circle' or 'circle':
    circle()
elif shape =='Square' or 'square':
    square()
elif shape =='rectangle' or 'Rectangle':
    rec()



#Q4
import sys
a=input("What type of intrest do you want to calculate Simple or Compound :")
def s():
    p=int(input("Enter the principal amount :"))
    t=int(input("Enter the time (in years)"))
    r=int(input("Enter the annual rate of intrest :"))
    A=p*(1+r*t)
    print("The Total Amount to be paid after",t,"years is",A)
    sys.exit()
def c():
    p=int(input("Enter the principal amount :"))
    t=int(input("Enter the time (in years)"))
    r=int(input("Enter the annual rate of intrest :"))
    n=int(input("Enter the amount of times the interest is compound per time period :"))
    C=p*(1+r/n)**nt
    print("The Total Amount to be paid after",t,"years is",C)
    sys.exit()
if a=='Simple' or 'simple':
    s()
if a=='Compound' or 'compound':
    c()


#Q5
cp=int(input("Enter the costing price of the product :"))
sp=int(input("Enter the selling price of the product :"))
profit=sp-cp
loss=cp-sp
print("The Profit is :",profit," and the Loss is :",loss)


#Q6
p=int(input("Enter the principal amount :"))
t=int(input("Enter the time (in months)"))
r=int(input("Enter the annual rate of intrest :"))
EMI=(p+r)/t
print("The EMI is :",EMI)

'''




    
