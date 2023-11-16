# A shop has the four products (pendrive, keyboard, mouse, and headphone). Take the prices and
# number of units for each product. Print the total amount to pay. The shop offers 25% discount if
# total cost is more than 2000 tk.

pendrive=int(input("Enter pendrive price: "))
pendrive_unit=int(input("Enter pendrive unit: "))
keyboard=int(input("Enter keyboard price: "))
keyboard_unit=int(input("Enter keyboard unit: "))
mouse=int(input("Enter mouse price: "))
mouse_unit=int(input("Enter mouse unit: "))
headphone=int(input("Enter headphone price: "))
headphone_unit=int(input("Enter headphone unit: "))
total_cost=pendrive*pendrive_unit+keyboard*keyboard_unit+mouse*mouse_unit+headphone*headphone_unit

# print("your pendrive price is", pendrive)
# print("your keyboard price is", keyboard)
# print("your mouse price is", mouse)
# print("your headphone price is", headphone)
# amount=(pendrive+ keyboard+ mouse+ headphone)
# print("your total ammount is", amount, "tk")

if total_cost>2000:
    print("you got 25% discount")
else:
    print("you can't got 25% discount")
topay= total_cost/100*75
print(" You have to pay", topay, "tk")
