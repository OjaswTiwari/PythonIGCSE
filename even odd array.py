num= []
for i in range (0,20):
    x= int(input("Enter a Number"))
    num.append(x)
even= 0
odd= 0
for j in range (0,20):
    if (num[j]%2==0):
        even=even+1
    else:
        odd=odd+1
print(odd," is the count of odd numbers")
print(even," is the count of even numbers")
