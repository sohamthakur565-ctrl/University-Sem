num=int(input("Enter the number to find the factorial: "))
fact=1
for i in range(1,num+1,1):
    fact=fact*i
print("The Factorial of ",num," is ",fact)
