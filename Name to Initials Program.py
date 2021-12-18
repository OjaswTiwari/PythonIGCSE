str=input("enter your full name")
str=" "+str
rev=""
for i in range(0, len(str)-1):
    x=str[i]
    if(x==' '):
        rev=rev+str[i+1]
print (rev)
