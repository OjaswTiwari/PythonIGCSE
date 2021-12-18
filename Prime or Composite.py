n=int(input("enter a number "))
def prime(n):
    x=0
    for i in range (2,n):
        if (n%i==0):
            x=x+1
    if(x==0):
        print(n,"is a prime number")
    else:
        print(n,"is not a prime number")
prime(n)
