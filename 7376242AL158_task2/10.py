num = int(input ("enter a number :"))
b =num 
rev =0
while b !=0:
    digit = b %10 
    rev = rev *10 + digit 
    b //=10

if rev == num :
    print("the given number is a mirror number ")
else:
    print("the given number is not a mirror number ")
    