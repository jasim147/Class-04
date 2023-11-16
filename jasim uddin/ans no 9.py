#A school has following rules for grading system:

#i) Below 50 – F; ii) 50 to 60 – D; iii) 60 to 70 – C; iv) 70 to 80 – B; v) Above 80 – A
#• Ask user to enter marks and print the corresponding grade.

#
# marks= int(input(" Enter your marks= "))
# if marks<50:
#     print("your grade is F")
# elif marks>=50 and marks<60:
#     print(" Your grade is D")
# elif marks>=60 and marks<70:
#     print(" Your grade is C")
# elif marks>=70 and marks<80:
#     print(" Your grade is B")
# elif marks >=80 and marks<=100:
#     print(" Your grade is A")
# if marks<0 or marks>100:
#     print(" Invalid mark")

mark=int(input(" Enter your marks="))
if mark<50 and mark>=0:
    print("You are fail")
elif mark>=50 and mark<60:
    print("Your grade is D")
elif mark>=60 and mark<70:
    print("your grade is C")
elif mark>=70 and mark<80:
    print("Your grade is B")
elif mark>=80 and mark<100:
    print("Your grade is A")
else:
    print("Invalid mark")