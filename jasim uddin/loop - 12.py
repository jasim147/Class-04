# Write a program to print the reverse of a number.
# number= int(input(" Enter a number you want to Reverse: "))
# print(str(number)[::-1])
n=int(input(" enter a number: "))
newNumber=0
if n%10==0:
    s1="0"
else:
    s1=""
while n!=0:
    digit=n%10
    newNumber=newNumber*10+digit
    n=n//10
    s2=str(newNumber)
print(s1+s2)
