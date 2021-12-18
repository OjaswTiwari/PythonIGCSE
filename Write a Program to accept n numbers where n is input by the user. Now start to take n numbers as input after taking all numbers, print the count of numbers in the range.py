number= []
n= int(input("Enter the number of input"))
count0to30= 0
count31to60= 0
count61to75= 0
count76to100= 0
countg= 0
while (countg<n):
    print ("Enter the number")
    x= int(input(""))
    number.append (x)
    if (x>=0 and x<=30):
        count0to30= count0to30+1
    elif (31<=x<=60):
        count31to60= count31to60+1
    elif (61<=x<=75):
        count61to75= count61to75+1
    elif (76<=x<=100):
        count76to100= count76to100+1
    else:
        print ("Invalid Input")
        continue
    countg= countg+1 
print ("0 to 30 :",count0to30)
print ("31 to 60",count31to60)
print ("61 to 75",count61to75)
print ("76 to 100",count76to100)
