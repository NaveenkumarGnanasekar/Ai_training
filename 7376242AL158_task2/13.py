def factorial(n):
    num =1
    for i in range (1,n+1):
        num *=i
    return num 
num = int (input ("enter a number:"))
b = num
sum =0 
while b !=0:
    num1 = b % 10
    fact= factorial(num1)
    sum +=fact
    b //=10
if sum == num :
    print("the given number is a strong number ")
else :
    print("the given number is not a strong number ")

