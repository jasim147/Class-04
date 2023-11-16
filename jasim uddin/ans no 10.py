# A company decided to give bonus to employees based on the following
# conditions:
# i. 10% of salary if year of service is more than 5 years
# ii. 5% of salary if year of service is more than 3 years.
# • Ask user for their salary and year of service and print the total amount.
# salary= int(input(" Enter yur salary: "))
# year= int(input(" Enter yur service year : "))
# total=salary*year
# if year>5:
#     print(" Congratulations! Your company give you 10% bonus")
#     salary1 = total *100/90
#     print("Your salary with bonus is =", salary1)
# elif year>3 and year:
#     salary2 = total* 100 / 95
#     print("Congratulations! Your company give you 5% bonus")
#     print("your salary with bonus is", salary2)
# else:
#     print("You are not eligable for bonus")


salary=int(input("Enter your year: "))
year= int(input("Enter your job year: "))
total=salary*year
if year>5:
    salary1 = total*100/90
    print("Congratulation! Your company give you 10% bonus")
    print("Yor salary with bonus is", salary1)
elif year>3 and year<5:
    salary2=salary/100*105
    print("Congratulation! Your company give you 5% bonus")
    print("Your salary is", salary2)
else:
    print("You are not eligable for bonus")