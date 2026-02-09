n = list(input("enter the dishes name :").split())
lst=[]
max1 =0
item =""
for i in n :
    c=n.count(i)
    if c > max1 :
        max1 = c
        item = i
    if c ==1 :
        lst.append(i)
print(f"the most ordered dish = {item}")
print(f"the dishes ordered exactly once = {lst}")