n = int(input("enter the pairs :"))
dict = {}
new_dict ={}
lst = []
for i in range (n):
    key = input("enter key(string):")
    value = int(input("enter value for the key(int) :"))
    dict.setdefault(key,value)
for key,value in dict.items():
    if value in lst:
        continue
    else:
        lst.append(value)    
        new_dict.setdefault(value,key)

print(new_dict)