n = int(input ("enter a number:"))
sum =0
while n !=0:
    sum += n %10
    n//=10
print("the sum of digits in the number is :", sum )