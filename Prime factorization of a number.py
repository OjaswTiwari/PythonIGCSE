n= int(input("Enter a number"))
i=2
while(n!=1):
   rem= n%i
   if(rem==0):
      n=n/i
      print(i)
   else:
      i=i+1
