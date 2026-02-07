n = list(map(int,input("enter list :").split()))
dict ={}
for i in n:
    if i in dict.keys():
        dict[i]+=1
    else:
        dict.setdefault(i,1)
n1=int(input("enter k value:"))
lst=[]
dict1=sorted(dict,key=dict.get)
for i in range (-1,-n1-1,-1):
    lst.append(dict1[i])
print(lst)