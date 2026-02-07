n = int(input("enter number of students:"))
dict ={}
for i in range(1,n+1):
    name = input(f"enter name of the student {i}:").lower()
    dept= input(f"enter department of the student {i}:").lower()
    dict.setdefault(name,dept)
new_dict={}
for i,j in dict.items():
    lst =[]
    if j in new_dict:
        new_dict[j].append(i)
    else:
        lst.append(i)
        new_dict.setdefault(j,lst)
print(new_dict)