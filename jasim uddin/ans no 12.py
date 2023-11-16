# classes_held= float(input("Enter the number of classes held: "))
# classes_attended= float(input("Enter the umber of classes attended: "))
# present= (classes_attended/classes_held)*100
# print("Your attendance is", present,"%")
# if present>=70:
#     print(" you can sit in the exam")
# else:
#     print(" You cat't sit in  the exam")

class_held=float(input("Enter the number of class held: "))
class_attend=float(input("Enter the class you attend:" ))
present=class_attend/class_held*100
print("you attend the class", present, "%")
if present>=70:
    print("You can sit in the exam")
else:
    print("You can't attend the exam. ")


