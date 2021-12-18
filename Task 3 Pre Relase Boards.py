#Task 3
#Line Count: 34
import random
MulNum = [2,3,4,5,6,7,8,9,10,11,12]
WholeNum = [1,2,3,4,5,6,7,8,9,10,11,12]
count=0
StudentName= input("Enter your name: ")
Question= int(input("How many question or questions do you need: "))
result=[]
for i in range (1,Question+1):
    print ("Question", i)
    flag=0
    while (flag==0):
        flag=1
        NumberMul= int(random.random()*11)
        NumberWhole= int(random.random()*10)
        ans= MulNum[NumberMul]*WholeNum[NumberWhole]
        if i==1:
            result.append(ans)
            break
        else:
            for j in range(0,len(result)):
                       if(ans==result[j]):
                           flag=0
                           break
    UserAns= int(input("%d *%d =" % (MulNum[NumberMul],WholeNum[NumberWhole])))
    if ans == UserAns:
        count=count+1
    else:
        print ("Wrong Answer")
if count==5:
    print (StudentName, "Your score is ", str(count), "/", Question)
    print ("Well Done")
else:
    print (StudentName, "Your score is: ", str(count), "/", Question)
    print ("Have another practice")



        
        
