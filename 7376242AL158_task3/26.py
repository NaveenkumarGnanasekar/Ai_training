n = list(map(int,input("enter list :").split()))
h=[x for x in n if x>=75]
m=[x for x in n if x<75 and x>=50 ]
l=[x for x in n if x<50]
dict={">=75":h,"74-50":m,"<50":l}
print(dict)