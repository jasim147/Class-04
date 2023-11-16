# # A shop will give discount of 10% if the cost of purchased quantity is more than
# # 1000.
# # • Ask user for quantity. Suppose, one unit will cost 100. Judge and print total cost for user.
# product=print(" each product is only 100 tk")
# product=100
# product_unit=int(input(" Enter product unit: "))
# total_cost=(product*product_unit)
# print("Your total cost is ", total_cost)
# if total_cost>1000:
#     print("After 10% discount. You have to pay", total_cost/100*90)

product= print("Eash product is only 100 tk.")
product=100
product_unit=int(input("Enter product unit"))
total_cost=(product*product_unit)
print("your total cost is", total_cost)
if total_cost>1000:
    print( "You got discount 10% tk. Your total cost is", total_cost/100*90 )
else:
    print("you have to pay", total_cost)