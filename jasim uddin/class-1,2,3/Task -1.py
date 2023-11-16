# A shop has the four products (pendrive, keyboard, mouse, and headphone). Take the prices of
# each products and print the total amount to pay. The shop offers 20% discount if total cost is
# more than 1000 tk

Pendrive=int(input("Enter pendrive price: "))
keyboard=int(input("Enter keyboard price: "))
mouse= int(input("Enter mouse price: "))
headphone= int(input("Enter headphone price: "))
totalcost=(Pendrive+keyboard+mouse+headphone)
print("Your total price is", totalcost,"tk")
if totalcost>1000:
    topay = totalcost / 100 * 80
else:
    topay= totalcost
print(" You have to pay", topay, "tk")