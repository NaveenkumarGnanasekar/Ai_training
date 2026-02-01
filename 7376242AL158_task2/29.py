num = int(input("enter the ticket number ") )
b = num 
sum =0 
while b !=0:
    digit = b%10 
    sum +=digit 
    b //=10 
if sum % 9 ==0 :
    print("valid ticket number ")
else :
    print("invalid ticket number ")


