# # Take input of age of 3 people by user and determine oldest and youngest
# # # among them.
# people1=int(input(" Enter first people age: "))
# people2=int(input(" Enter second people age: "))
# people3=int(input(" Enter third people age: "))
# oldest= max(people1, people2, people3)
# youngest= min(people1, people2, people3)
# print("Oldest age is", oldest, "years old")
# print("yongest age is",youngest, " Years old" )

p1=int(input("Enter first people age: "))
p2=int(input("Enter 2nd p age: "))
p3=int(input("Enter 3rd p age: "))
if p1>p2:
    large=p1
else:
    large=p2
if p3>large:
    large=p3
print("the largest number is ", large)



