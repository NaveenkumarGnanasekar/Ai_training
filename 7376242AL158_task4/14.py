n = list(input("enter passwords with space :").split())
lst=[]
special1=["!","@","#","$","%","^","&","*","<",">"]
for i in n :
    digit=False
    special = False
    for j in i :
        if j.isdigit():
            digit=True
        elif j in special1:
            special=True
    if digit and special:
        t=(i,"valid")
        lst.append(t)
    else:
        t = (i,"Inavlid")
        lst.append(t)
print(lst)