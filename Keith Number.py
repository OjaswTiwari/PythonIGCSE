c = input("enter a no")
l = len(c)
num=int (c)
n=num
b=[]
sum=0
print (num)
print (l)
for i in range (0,l):
    b.append(int(c[i]))
    sum= sum+b[i]
print (b)
print(sum)
while (sum <n):
    for i in range (1,l):
        b[i - 1] = b[i]
    b[l - 1] = sum
    sum = 0;
    for k in range (0,l): 
        sum = sum + b[k];  
if (sum == n):
    print ("Its a keith no")
else:
    print("its not a keith number")
