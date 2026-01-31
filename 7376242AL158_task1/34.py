n = int(input ("enter a number :"))
count =0
sum =0
b=n
c =n  
while n !=0:
    count +=1
    n //=10
while b !=0:
    sum += (b %10)**count 
    b //=10
if sum == c :
    print("it is a armstrong number ")
else:
    print("it is not a armstrong number ")
