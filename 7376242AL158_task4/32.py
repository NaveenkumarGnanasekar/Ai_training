n = int(input("enter number of candidate :"))
dict = {} 
dict1 ={}
lst=[]
for i in range (1,n+1):
    candidate = input("enter name of candidate:")
    lst1=list(map(int,input("enter years of experience per job:").split()))
    dict[candidate]=lst1
    total= sum (lst1)
    dict1[candidate]=total
num = int(input("enter company average :"))
for i,j in dict1.items():
    if j > num:
        t=(i,j)
        lst.append(t)
print(dict1)
print(lst)
