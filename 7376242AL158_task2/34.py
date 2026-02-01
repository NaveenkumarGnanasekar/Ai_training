n = int(input ("enter the number of days :"))
sum =0 
for i in range (1,n+1):
    value = int(input (f"enter the rainfall value of {i}:"))
    sum +=value
avg = sum / n
print(f"the average rainfall of {n}days = {avg}")