product_quantity= int(input("Enter product quantity: "))
product_unit=int(input("Enter product unit: "))
parcent=int(input(" Enter percent"))
price=product_quantity*product_unit
to_pay=price
# dis_price=price-(price*(100/parcent))
if price>=2000:
    dis_price = price-(price * (100 / parcent))
    print("You got", parcent,"% discount. You have to pay", dis_price)
else:
    print(" You have to pay: ", to_pay)
