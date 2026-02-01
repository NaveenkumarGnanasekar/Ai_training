num = int(input ("enter a number:"))
b = num 
last_digit = True 
num1 = num  % 100
change = 0 

while b != 0 :
    digit = num1 %10  
    if last_digit :
        if digit >=0 and digit <=4:
            change = -1
        else :
            change = +1
    else:
        if change == -1 :
            digit = (digit - 1) *10 
        else :
            digit = (digit) *10         
    last_digit= False
    b //=10
num //=100

num = num *100 + digit
print("Number after rounding off =", num )

