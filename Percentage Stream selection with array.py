student_id= []
student_name= []
percentage= []
sci=0
com=0
hum=0
size= int(input("Enter the number of student entry"))
for i in range (0,size):
    id= int(input("enter your ID"))
    student_id.append(id)
    name= input("Enter name: ")
    student_name.append(name)
    per= float(input("Enter percentage: "))
    percentage.append(per)
    if (per>=80):
        sci= sci+1
    elif (per>60):
        com=com+1
    else:
        hum=hum+1
print ("No. of students in Science stream: ", sci)
print ("No. of students in Commerce stream: ", com)
print ("No. of students in Humanities stream: ", hum)
