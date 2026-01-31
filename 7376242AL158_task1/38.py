n = int (input("enter a number :"))
count =0 
for i in range (1 , n+1):
    if n % i ==0:
        count +=1
    else:
        continue
print("the number of factors of the number is :", count )
