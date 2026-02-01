n = int (input ("enter the lock number :"))
zero_flag =0 
last_digit = n %10 
b = n //10 
while b !=0:
    num= b %10
    if num ==0:
        zero_flag= 1
    b //=10
if last_digit == 5 and zero_flag ==1:
    print("lock open ")
else :
    print("invalid lock number ")