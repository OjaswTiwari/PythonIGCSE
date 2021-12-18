charity1= []
charity2= []
charity3= []
bill_amount= float(input("Enter the Bill Amount"))
if (bill_amount<=0):
    print("Wrong Input")
charity_amount= bill_amount*0.01
final= charity_amount+bill_amount
x= int(input("Do you want to donate to a charity, Press 1 for Yes and 0 for No"))
if (x==1):
    charity_choice= int(input("If you want to donate to MakeAWish press 1, If you want to donate to Orphange Press 2, If you want to donate to Old Age Home Press 3"))
        if (charity_choice==1):
            charity1.append (charity_amount)
                print("You final bill is, ", final)
        elif (charity_choice==2):
            charity2.append (charity_amount)
                print("You final bill is, ", final)
        elif (chairty_choice==3):
            charity3.append (chairty_amount)
                print("You final bill is, ", final)
        else:
            print("Wrong Input")
if (x==0):
    then print("Your final bill is, "bill_amount)


                
             
    
