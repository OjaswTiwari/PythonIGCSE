import random
StudentName= input("Enter your name: ")
count= 0
NumberOfQuestion= 1
while(True):
    ChoiceMul = int(input("Enter the choice of multiplication table: "))
    if ChoiceMul<= 12 and ChoiceMul>=2:
        break
    else:
        print ("Invalid number and Enter 2 to 12")
Qu=[]
while(True):
    print ("Question ", NumberOfQuestion)
    num= int(random.random()*11)+1
    if NumberOfQuestion==1:
        Qu.append(num)
    else:
            for j in range (0, len(Qu)):
                if num==Qu[j]:
                    print (num)
                    num= int(random.random()*11)+1
            Qu.append(num)         
   
    answer= int(input("%d * %d =" % (ChoiceMul,num)))
        
    if answer==(num*ChoiceMul):
        count= count+1
        print ("correct answer")
    else:
        print ("wrong answer")
    NumberOfQuestion= NumberOfQuestion+1
    if NumberOfQuestion>5 :
        break
if count==5:
    print (StudentName, "Your score is ", str(count), "/5")
    print ("Well Done")
else:
    print (StudentName, "Your score is: ", str(count), "/5")
    print ("Have another practice")
