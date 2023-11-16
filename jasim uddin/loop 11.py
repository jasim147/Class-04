# Write a program to display the multiplication table of a given integer.

# number = int(input ("Enter the number of which the user wants to print the multiplication table: "))
# # We are using "for loop" to iterate the multiplication 10 times
# print ("The Multiplication Table of: ", number)
# for count in range(1, 11):
#    print (number, 'x', count, '=', number * count)
# number = int(input("Enter the number for multiplication: "))
# i = 1
# # for count in range(1, 11):
# while i <= 10:
#    mul = i * number
#    print(number, 'x', i, '=', mul)
#    i = i + 1

n=int(input("Enter the number you want to multiplication"))
i=1
while i<=10:
   mul=i*n
   print(n, "*", i,"=", mul)
   i=i+1

