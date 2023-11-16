n1=float(input("Enter first number: "))
n2=float(input("Enter second number: "))
n3=float(input("Enter third number: "))
if n1>n2:
    large=n1
else:
    large=n2
if n3>large:
    large=n3
print(large, "is the largest number",)