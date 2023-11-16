# 1. Write a program to accept two integers and check whether they are equal or
# not.
number1= int(input(" Enter first number : "))
number2= int(input(" Enter second number : "))
if number1==number2:
    print("equal")
else:
    print(" Not equal")

# 2. Write a program to check whether a given number is even or odd.
number1= int(input(" Enter first number : "))
div=number1/2
if number1==0:
    print(" This number is a even number. ")

else:
    print(" It is a odd number. ")



# 3. Write a program to read the age of a candidate and determine whether s/he is
# eligible for casting vote.
age=int(input(" Enter your age: "))
if age >18:
    print(" You are a votar")
else:
    print(" You are child. Your are not a votar")

# 4. Write a program to find the largest of three numbers.
number1= float(input(" Enter the first number : "))
number2= float(input(" Enter the second number: "))
number3= float(input(" Enter the third number: "))
if number1>number2:
    large=number1
else:
    large=number2
if number3>large:
    large=number3
print(large, " is the largerst number. " )

# 5. Write a program to find the smallest of three numbers.
number1=float(input("Enter first number: "))
number2=float(input(" Enter second number: "))
number3= float(input(" Enter third number:"))
if number1<number2:
    small=number1
else:
    small= number2
if number3<small:
    small=number3
print(small, " is the smolest number. ")

# 6. write a program using python to create a simple calculator
number1=float(input("Enter first number : "))
number2= float(input(" Enter second number: "))
opr=float(input(" Enter an Oparetor"))
if opr=="+":
    print(number1+number2)
elif opr=="-":
    print(number1-number2)
elif opr=="*":
    print(number1*number2)
elif opr=="/":
    print(number1/number2)
elif opr=="%":
    print(number1/100*number2, "%")
else:
    print(" Invalid number. ")


# 7. Write a program to accept a coordinate point in a XY coordinate system and
# determine in which quadrant the coordinate point lies.