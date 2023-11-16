age=int(input("age: "))
gender= input(" gender: ")
if gender=="male":
    if age>=20:
        print("eligible")
    else:
        print(" Not eligible")
elif gender=="famale":
    if age>=18:
        print("eligible")
    else:
        print(" not eligible")