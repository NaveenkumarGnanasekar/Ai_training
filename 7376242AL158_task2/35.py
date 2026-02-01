num = int(input ("enter the lock pin :"))
count = 0 
b =num
sum =0 
while b !=0 :
    digit = b %10 
    sum +=digit 
    count+=1
    b //=10
if count ==4 and sum > 15 :
    print("ACCESS GRANTED")
else :
    print("ACCESS DENIED")