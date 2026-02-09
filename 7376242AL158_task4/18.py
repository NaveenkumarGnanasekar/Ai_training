n = list(input("enter filenames with space :").split())
dict={}
for i in n :
    j = i.split(".")
    if j[1] in dict :
        dict[j[1]]+=1
    else:
        dict[j[1]]=1
print(f"files grouped with extension :{dict}")