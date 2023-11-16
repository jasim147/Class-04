#use if , elif, else
gender=input("Enter your gender: ")
age= int(input("Enter your age: "))
if gender=="male" and age>=21:
    print("Congrats! You can marry.")
elif gender=="female" and age>=18:
    print("Congrats! You can't marry.")
else:
    print("Sorry! You can marry. ")
