n = int(input ("enter password:"))
last_even = False
last_digit = True
sum = 0 
b =n 
digit = 0 
while n !=0:
    digit = n %10
    if last_even and digit %2 ==0:
        last_even = True
        sum +=digit  
    else :
        sum +=digit 
    n //=10
if sum %3 ==0 and last_even:
    print("password correct  ")
else :
    print("invalid password ")

    