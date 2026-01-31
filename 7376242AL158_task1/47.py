n = int (input ("enter a number :"))
b =n 
digit =0
while n !=0:
    digit +=n%10
    n //=10
if b %digit ==0:
    print(b , "is a harshad number ")
else :
    print(b , "is not a harshad number ")
