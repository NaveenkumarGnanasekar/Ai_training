num = int(input ("enter the number of floor :"))


for i in range (1, num+1):
    b =i
    flag =0 
    while b !=0:
        num1 = b %10 
        if num1 == 4:
            flag =1
        b //=10
    if flag == 1 :
        continue
    else :
        print(i)



