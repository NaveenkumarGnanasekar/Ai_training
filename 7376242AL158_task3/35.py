n = int(input("enter number of key:value pair:"))
dict={}
for i in range(1,n+1):
    key = input(f"enter key of element {i} :")
    values = input(f"enter value of element {i}:")
    dict.setdefault(key,values)
n1=dict.keys()
max1 =max(n1)
print(f"key with high value :{max1}")