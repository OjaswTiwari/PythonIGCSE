a= int(input("Enter number 1 "))
b= int(input("Enter number 2 "))
while True:
    rem=b%a
    if (rem==0):
        gcd=a
        break
    elif (rem==1):
        gcd=1
        break
    else:
        b=a
        a=rem
print ("the GCD is",gcd)
