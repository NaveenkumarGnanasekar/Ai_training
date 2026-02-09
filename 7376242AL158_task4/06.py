n = int(input("enter number of employee:"))
dict={}
lst=[]
lst1=[]
for i in range(1,n+1):
    name = input(f"enter name of employee {i} :")
    skills = list(input("enter skills of employee with space:").lower().split())
    lst.append(set(skills))
    dict[name]=skills
for j,i in dict.items():
    if "sql" in i and "python" in i:
        lst1.append[j]
common = set.intersection(*lst)
u=set.union(*lst)
print(common, "is skills all the employee.")

print(u,"is skills which atleast one employee know")