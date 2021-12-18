array= []
array_size= int(input("Enter size of array"))
high= array [0]
for i in range (0, array_size):
    array= [i]
    x= input("Enter the number")
    array.append (x)
    if (x>high):
        high=x
    else:
        continue
print(high)
