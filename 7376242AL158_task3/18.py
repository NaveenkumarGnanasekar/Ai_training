n = int(input("enter number of students :"))
dict = {}
new_dict ={}
for i in range (1,n+1):
    name = input(f"enter the name of the student {i}:")
    marks = list(map(int, input(f"enter the marks of the student {i} :").split()))
    avg = sum(marks)/len(marks)
    new_dict.setdefault(name,avg)
    dict.setdefault(name,marks)
print(f"the average mark of the given students with name = {new_dict}")