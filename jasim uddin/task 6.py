n1=float(input("Enter first number: "))
n2=float(input("Enter second number: "))
n3=float(input("Enter third number: "))
if n1<n2:
    small=n1
else:
    small=n2
if n3<small:
    small=n3
print(small, "is the smallest number",)