n = list(input("enter a sentence:").split())
dict={}
for i in n :
    lst=[]
    if len(i) in dict.keys():
        dict[len(i)].append(i)
    else:
        lst.append(i)
        dict.setdefault(len(i),lst)
print(dict)