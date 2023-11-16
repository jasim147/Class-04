# Write a program to print the sum of digits in a number.

num = input("Enter Number: ")
i=1
sum = 0

for i in num:
    sum = sum + int(i)

print("Sum of", num, "is = ", sum)