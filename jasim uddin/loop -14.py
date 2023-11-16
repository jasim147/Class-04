
# 14. Write a program to display Fibonacci series up to 10 terms.
# n=int(input(" Number of terms: "))
# a=0
# b=1
# count=3
# while count<=n:
#     c=a+b
#     print(c)
#     a=b
#     b=c
#     count =count+1

n=int(input(" Number of terms : "))
a=0
b=1
count=1
while count<=n:
    c=a+b
    print(c)
    a=b
    b=c
    count=count+1