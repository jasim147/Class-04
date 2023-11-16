pendrive=int(input("Enter pendrive price: "))
pendrive_unit=int(input("Enter pendrive unit: "))
keyboard=int(input("Enter keyboard price: "))
keyboard_unit=int(input("Enter keyboard unit: "))
mouse=int(input("Enter mouse price: "))
mouse_unit=int(input("Enter mouse unit: "))
headphone=int(input("Enter headphone price: "))
headphone_unit=int(input("Enter headphone unit: "))
totalcost=pendrive*pendrive_unit+keyboard*keyboard_unit+mouse*mouse_unit+headphone*headphone_unit

# print("your pendrive price is", pendrive)
# print("your keyboard price is", keyboard)
# print("your mouse price is", mouse)
# print("your headphone price is", headphone)
# amount=(pendrive+ keyboard+ mouse+ headphone)
# print("your total ammount is", amount, "tk")
if totalcost>=2000:
    topay = totalcost/100 * 75
else:
    topay= totalcost
print(" You have to pay", topay, "tk")
