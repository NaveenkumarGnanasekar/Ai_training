base = int(input("enter the base number :"))
exponent = int(input("enter the expoenent number :"))
answer =1 
for i in range (exponent):
    answer *=base
print(base , "raised to the power" , exponent , "is" , answer )