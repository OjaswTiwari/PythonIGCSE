str= input("Enter a String: ")
rev=""
for i in range (0,len(str)):
    x=str[i]
    if(x.isupper()):
        rev= rev+x.lower()
    elif(x.islower()):
        rev= rev+x.upper()
    else:
        rev=rev+x
print("Orignal String is: ",str)
print("The String in toggle case is: ",rev)
        
    
