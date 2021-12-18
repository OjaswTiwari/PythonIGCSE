name=[]
size= int(input("Enter the Number of names you want to enter: "))
for i in range (0,size):
    n= input("Enter Name: ")
    name.append(n)
print("The names begining with A are")
for j in range (0,size):
    x= name[j]
    if (x[0]=='A' or x[0]=='a'):
        print (n)
    
