# x=int(input("Enter first number:"))
# y=int(input("Enter second number:"))
# if x>0 and y>0:
#     print("coordinate 1 ")
# elif x>0 and y<0:
#     print("coordinate 2 ")
# elif x < 0 and y < 0:
#     print("coordinate 3 ")
# elif x < 0 and y> 0:
#     print("coordinate 4 ")


# Write a program to accept a coordinate point in a XY coordinate system and
# determine in which quadrant the coordinate point lies.

x=int(input("Enter first number: "))
y= int(input(" Enter the second number: "))
if x>0 and y>0:
    print("cordinate 1")
elif x>0 and y<0:
    print("cordinate 2")
elif x<0 and y<0:
    print("cordinate 3")
elif x<0 and y>0:
    print("cordinate 4")