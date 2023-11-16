#
# 2) A company decided to give bonus to employees based on the following conditions:
# a) 15% of salary if year of service is more than 10 years;
# b) 10% of salary if year of service is more than 5 years;
# c) 5% of salary otherwise;
# • Ask user for their salary and year of service and print the total amount.

salary=int(input("Enter Your salary: "))
year=int(input("Enter your year: "))
total=salary*year
if year>10:
    total_salary1=total/100*115
    print("Your company give you 15% bonus. Now your salary with bonus is", total_salary1)
elif year>5 and year<=10:
    total_salary2=total/100*110
    print("Your company give you 10% bonus. Now your salary with bonus is", total_salary2)
elif year<=5:
    total_salary3=total/100*105
    print("Your company give you 5% bonus. Now your salary with bonus is", total_salary3)
