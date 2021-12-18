import math
n=int(input("enter a number"))
num=int(n)
c=0
while(n!=0):
    c=c+1
    n=n//10
c=c-1
for i in range (c, -1, -1):
    print(num//math.pow(10,i))
