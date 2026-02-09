n = int(input("enter the number of students:"))
dict={}
for i in range(1,n+1):
    name = input(f"enter name of student {i}")
    mod = list(input("enter modules completed :").split())
    dict[name]=mod
lst=[len(j) for i,j in dict.items()]
lst1=sorted(list(zip(dict.keys(),lst)),key=lambda x :x[1])
print(lst1)
print(f"student who completed max module :{lst1[-1]}")