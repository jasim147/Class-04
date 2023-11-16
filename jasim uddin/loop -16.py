
# Write a program to determine whether a given number is prime or not.
# n=int(input(" Enter the number: "))
# i=2
# prime=True
# while i<n:
#     mod=n%i
#     if mod==0:
#         prime=False
#         break
#     i=i+1
# if prime==True:
#     print(n, "is a prime number")
# else:
#     print(n, "is not a prime number.")
n=int(input(" Enter the number : "))
i=2
prime=True
while i<n:
    mod=n%1
    if mod==0:
        prime=False
        break
    i=i+1
if prime==True:
    print(n," is a prime number.")
else:
    print(n," is not a prime number.")