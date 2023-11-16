# 3) Write a program to read marks of n students and find their average mark.

n=int(input(" Enter students : "))
i=1
sum=0
while i<=n:
    number=float(input(" Enter their marks : "))
    sum=sum+number
    i=i+1
avr=sum/n
print("The agarege of ",n," number is ", avr)