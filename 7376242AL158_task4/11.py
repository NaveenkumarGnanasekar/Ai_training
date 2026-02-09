rs={"python","c++","c","ros","ml"}
n = int(input("enter the number of resume:"))
lst =[]
dict={}
for i in range(1,n+1):
    s=set(input("enter skills : ").split())
    common = rs.intersection(s)
    uni=rs.union(s)
    percentange = len(common)/len(uni)
    if percentange >0.7:
        lst.append(i)
    dict[i]=rs.difference(s)
print(f"the missing skills of each person :{dict}")
print(f"resume numbers with skill more the 70% : {lst}")