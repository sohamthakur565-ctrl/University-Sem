num=int(input("How many elements you want to enter: "))
count=0
list_1=[]
while num>count:
    user_input=int(input("Enter the element (takes only 10): "))
    list_1.append(user_input)
    count+=1
sum=0
avg=0
for i in range(0,(len(list_1)),1):
    sum=sum+list_1[i]
avg=sum/len(list_1)
print("Sum of list:",sum)
print("Average of list:",avg)
