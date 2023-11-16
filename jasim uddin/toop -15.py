
# 15. Write a program to check whether a given number is a 'Perfect' number or
# not. Perfect number, a positive integer that is equal to the sum of its
# proper divisors. The smallest perfect number is 6, which is the sum of 1, 2,
# and 3.
# n=int(input(" Enter the number: "))
# i=1
# sum=0
# while i<n:
#     mod=n%i
#     if mod==0:
#         sum=sum+i
#     i=i+1
# if sum==n:
#      print(n, "is a perfect number. ")
# else:
#     print(n, "is not a perfect number. ")

n=int(input(" Enter the number: "))
i=1
sum=0
while i<n:
    mod=n%1
    if mod==0:
        sum=sum+1
    i=i=1
if sum==n:
    print(n," Is the parfect number. ")
else:
    print(n, " is not a perfect number. ")