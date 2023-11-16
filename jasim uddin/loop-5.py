# Write a program to calculate the factorial of a given number.

n = int(input("Enter a number: "))
i=1
factorial = 1
while i<=n:
    factorial = factorial * i
    print(i, "The factorial number is ", factorial)
    i = i + 1
print("complete")
