#Task 2
#Line Count:
import random
StudentName = input("Enter your name: ")
count= 0
NumberOfQuestions = 1
Question=[]
while(True):
    ChoiceMul= int(input("Enter your choice of Multiplication table : "))
    if ChoiceMul<=12 and ChoiceMul>=2 :
        break
    else:
        print ("Invalid number and Enter a number between 2 to 12")
while(True):
    print ("Question ",NumberOfQuestions)
    num= int(random.random()*11)+1
    attempt = 1
    num= int(random.random()*11)+1
    if NumberOfQuestions==1:
        Question.append(num)
    else:
        for j in range (0, len(Question)):
              if num==Question[j]:
                num= int(random.random()*11)+1
                j=0
        Question.append(num)           
    t=0    
    for attempt in range (0,3):
        answer= int(input("%d * %d =" % (ChoiceMul,num)))
        if answer>(num*ChoiceMul):
            print (StudentName, " your answer is too large")
        elif answer<(num*ChoiceMul):
            print (StudentName, " your answer is too low")
        elif answer==(num*ChoiceMul):
            print (StudentName, " your answer is correct")
            t=1
            break
    if t==0:
        print("Sorry your attempts are over. The correct answer to this problem is", num*ChoiceMul)      
    NumberOfQuestions= NumberOfQuestions+1
    if NumberOfQuestions> 5:
        break

    
