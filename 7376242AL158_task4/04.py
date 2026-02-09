key = list(input("enter item in dictionary 1:").split())
value = list(input("enter quantity of the items :").split())
key1 = list(input("enter item in dictionary 2:").split())
value1 = list(input("enter quantity of the items :").split())
dict1={}
dict2={}
dict3 = {}
for i,j in zip(key,value):
    dict1[i]=j
for i ,j in zip(key1,value1):
    dict2[i]=j
for i in dict1.keys():
    for j in dict2.keys():
        if i == j :
            dict1[i]=int(dict1[i]) + int(dict2[j])
        else:
            dict3[j]=int(dict2[j])
dict1 = dict1 | dict3
print(dict1)
