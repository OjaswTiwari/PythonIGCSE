count= 0
while (count<10):
    x=int(input("Enter the number"))
    if (x>=0 and x<=50):
        count= count+1
    elif(x<=0):
        print ("Please enter positive numbers only")
    else:
        print ("Invalid Input you have entered a number greater than 50")
        break
print (count)

        
