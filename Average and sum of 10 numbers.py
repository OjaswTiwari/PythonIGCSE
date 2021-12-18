sum=0
count=0
while (count<10) :
    num=int(input("Enter number: "))
    if(num>0):
        sum=sum+num
    else:
        print("Invalid input")
        continue
    count=count+1
avg=sum/10 
print("The sum is: ", sum)
print("Average: ",avg)
