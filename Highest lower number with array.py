num_size= int(input("Enter the number of elements"))
num= [num_size]
print ("Enter the first number")
num[0]= int(input())
low= num[0]
high= num[0]
for i in range (0,num_size):
    x= int(input("Enter numbers"))
    num.append (x)
    if (x>high):
        high= x
    if (x<low):
        low= x
print ("highest number is", high)
print ("lowest number is", low)

        
