n = int(input ("enter coupon number:" ))
sum = 0 
product =1
b =n 
while b !=0:
    num = b%10
    sum +=num 
    product *=num
    b//=10
if sum %2 ==0 and product %3 ==0 :
    print("valid coupon number ")
else :
    print("the coupon number is not valid ")
    