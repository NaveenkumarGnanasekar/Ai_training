num1 = int (input ("enter number1 :" ))
num2 = int (input ("enter number2 :" ))
small =0
big = 0 

if num1 <num2 :
    small =num1 
    big = num2 
else :
    small = num2 
    big = num1 
for i in range (big, 0, -1):
    if (small % i ==0 ) and (big % i ==0):
        gcf=i
        break 
lcm = (num1 * num2 ) // gcf
print(lcm, "is the lcm of ,", num1 , "and", num2 )
                   