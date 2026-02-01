n = int(input ("enter a number :"))
b =n 
flag = 0 
rev =0 
while b != 0 :
    num = b %10
    rev = rev * 10 + num 
    b //=10

for i in range (2, (n//2) ):
     if rev%i==0 :
        flag =1
if flag == 0 :
    print("the reverse of the given number is a prime number")
else :
    print("the reverse of the given numebr is not a prime number ")