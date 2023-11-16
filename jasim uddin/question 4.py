

# Write a program to find the largest of three numbers.


# number1=float(input("Enter first number: "))
# number2=float(input("Enter second number: "))
# number3=float(input("Enter third number: "))
# if number1>number2:
#     large=number1
# else:
#     large=number2
# if number3>large:
#     large=number3
# print(large, " is the large number. ")

n1=float(input("Enter first number"))
n2=float(input("Enter the second number"))
n3= float(input("Enter the third number "))
if n1>n2:
    large=n1
else:
    large=n2
if n3>large:
    large=n3
print(large,"is the largest number")