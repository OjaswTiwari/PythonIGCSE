#Task 1
#Line Count: 39 
import random
StudentName= input("Enter your name: ")
count= 0
NumberOfQuestion= 1
while(True):
    ChoiceMul = int(input("Enter the choice of multiplication table: "))
    if ChoiceMul>=2 and ChoiceMul<=12:
        break
    else:
        print ("Invalid number and Enter 2 to 12")
Question=[]
while(True):
    print ("Question ", NumberOfQuestion)
    num= int(random.random()*11)+1
    if NumberOfQuestion==1:
        Question.append(num)
    else:
            for j in range (0, len(Question)):
                if num==Question[j]:
                    print (num)
                    num= int(random.random()*11)+1
            Question.append(num)         
   
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
