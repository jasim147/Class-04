# 1) Write a C program to convert specified days into years, months and days.
#  Input: 400
#  Output: 1 year 1 month 5 days

day=int(input(" Enter Days: "))
year=day//365
month=(day%365)//30
days=(day%365)%30
print(year, " Year", month, " Month", days, "days")