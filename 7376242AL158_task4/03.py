n = int(input("enter number of students:"))
lst=[]
names=[]
slot=[]
for i in range(1,n+1):
    name = input(f"enter name of the student {i}:")
    slot_n=int(input(f"enter slot number of the student {i}:"))
    t=(name,slot)
    lst.append(t)
    names.append(name)
    slot.append(slot_n)

name_s=set(name)
slot_s=set(slot)
if len(name_s) == len(name) and len(slot)==len(slot_s):
    print("valid assignment")
else:
    print("invalid assignment")