number= []
size= int(input("Give size of the array"))
negative= 0
positive= 0
zero= 0
for i in range (0,size):
    x= int(input("Enter a number"))
    number.append(x)
    if(x>0):
        positive= positive+1
    elif (x<0):
        negative= negative+1
    else:
        zero= zero+1
print("The count of postive number is", positive)
print("The count of negative number is", negative)
print("The count of zero's is ", zero)        
