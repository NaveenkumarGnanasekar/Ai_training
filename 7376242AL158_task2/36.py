amount = int (input ("enter total shoppiing amount:"))
last_digit = amount % 10 
if amount >=3000 and last_digit==0:
    print("Yes")
else :
    print("No")
    