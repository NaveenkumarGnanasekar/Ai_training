n = int(input ("enter a number :"))
product=1
while n !=0:
    product *=n%10
    n//=10
print("the product of digits in the number is :",product )