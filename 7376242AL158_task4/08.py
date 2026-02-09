n = int(input("enter number of week:"))
lst=[]
for i in range(1,n+1):
    num = list(map(int,input(f"enter week {i} temperature :").split()))
    lst.append(num)
total_avg=0
max1=0
index=0
max_avg=0
lst1=[]
for i in lst:
    sum1 = sum(i)
    avg=sum1/len(i)
    lst1.append(avg)
    if avg > max_avg:
        max_avg= avg
        index=i
        total_avg+=avg
    else:
        total_avg=avg


    for j in i:
        if j > max1:
            max1=j
print(lst1,"the weekly average")
print(f"hottest temperature recorded :{max1}")
print("week",(lst1.index(max(lst1)))+1,"has the highest average")

