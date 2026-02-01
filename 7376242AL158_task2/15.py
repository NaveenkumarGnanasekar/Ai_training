price = int(input("enter the total price :"))
final_price = 0 
discount = 0 
if price <1000:
    final_price = price 
    discount = 0
    print("No discount ")
elif price >=1000 and price <3000:
    discount = price * 0.1
    final_price = price - discount
elif price >=3000 and price < 5000:
    discount = price * 0.2 
    final_price = price - discount 
elif price <= 5000:
    discount = price *0.3
    final_price = price - discount
else :
    print("invalid amount ")
print("the final price after discount amount of", discount ,"is", final_price)