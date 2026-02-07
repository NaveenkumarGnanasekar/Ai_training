data = list(map(int,input("enter list :").split()))
remove_list = list(map(int,input("enter the elements to be removed :").split()))
for i in remove_list:
    data.remove(i)
print(f"the final list :{data}")