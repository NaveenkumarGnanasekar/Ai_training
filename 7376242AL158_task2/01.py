n = int(input("enter a number n :"))
first = 0 
second =0
b =n
count  = 0 

while n !=0:
    count +=1
    n //=10 
m = count 
if count % 2 !=0:
    print("valid number , odd number of digits ")

else :
    while b !=0:
        digit = b %10 
        b //=10 
        count -=1
        if count >= (m //2):
            first +=digit 
        else :
            second +=digit
    if first == second :
        print("the given number is a balanced number ")
    else :
        print("the given number is not a balanced number ")