n= int(input("Enter a number :"))
def checkPalin (n):    
    rev= 0
    num= int(n)
    digit= 0
    while (n!=0):
        digit= n%10
        rev= rev*10+digit
        n= n//10
    if (num==rev):
        print (num, "is a palindrome number")
    else:
        print (num, "is not a palindrome")   
checkPalin (n)
