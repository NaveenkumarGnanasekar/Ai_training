age = int(input ("enter your age:"))
ticket_price = 200
final_price = 0 
if age < 5 :
    final_price = 0 
elif age >=5 and age <=12:
    final_price = 0.5 * ticket_price
elif age >=13 and age <=59:
    final_price = ticket_price
else :
    final_price = 0.3 * ticket_price
print("price of your ticket is ", final_price)
