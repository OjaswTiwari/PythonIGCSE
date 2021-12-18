#Write the psuedocode to accept a number and print its 10 multiple table. Also Print a count of its even multiples.
even=0
num= int(input("Enter a Number : "))
for i in range (1,11):
    e= num*i
    print (e)
    if (e%2==0):
        even=even+1         
print ( even, ": COUNT OF EVEN NUMBERS")
