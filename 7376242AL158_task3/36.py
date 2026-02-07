n = {"a":8,"b":7,"c":6}
m = {"a":9,"b":9,"c":5}
n1={}
for i,j in n.items():
    for k,l in m.items():
        if i == k:
            j=int(j)+int(l)
            n1.setdefault(i,j)
print(n1)
