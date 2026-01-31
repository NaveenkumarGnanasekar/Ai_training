a  = int (input("enter  number1:"))
b = int (input("enter  number2:"))
c = a+b 
d = a*b 
if c > d:
    print("(a+b) is greater than (a*b)")
elif d > c:
    print("(a*b) is greater than (a+b)")
else:
    print("(a+b) is equal to (a*b)")