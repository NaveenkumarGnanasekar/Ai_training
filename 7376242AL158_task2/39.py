k = int(input("enter time that the medicine has to be taken:"))
n = int(input ("enter total hours:"))
count = 0 
for i in range (0,n):
    if i % k ==0:
        count+=1
    else :
        continue
print(count)