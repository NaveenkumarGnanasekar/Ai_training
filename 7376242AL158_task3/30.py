n = list (map(int,input("enter a list :").split()))
n_s = [i**2 for i in n ]
lst=[]
for j,k in zip(n,n_s):
    t =(j,k)
    lst.append(t)
print("list of tuple:",lst)