pro_price = int(input ("enter the price of the product(per kg) :"))
weight = int(input ("enter the weight of product :"))
total_price =0
discount =0
price = pro_price * weight
if weight > 10 :
    discount = 0.15 * price 
    total_price = price - discount
    print("total amount =", total_price) 
else :
    print("total amount = ", price)