n = list(input("enter document 1 :").split())
m = list(input("enter document 2 :").split())
ns = set(n)
ms=set(m)
common = ns.intersection(ms)
un=ns.union(ms)
j_s=len(common)/len(un)
if j_s >=0.5:
    print("the given two documents are similar. ")
else:
    print("the given two document are not similar .")