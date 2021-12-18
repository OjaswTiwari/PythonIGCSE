num= int(input("Enter a number to check: "))
n= num
flag= 0
while (num!=0):
    digit= int(num%10)
    if(digit==0 or digit==1):
        num= num/10
        continue
    else:
        flag= flag+1
        break
if (flag==0):
    print (n, "is a binary number")
else:
    print (n, "is not a binary number")
