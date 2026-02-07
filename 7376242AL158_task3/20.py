n = input("enter a string:")
sp = ["@",",","!","#","$","%","^","&","*","(",")","<",">"]
digi_c=0
alpha_c=0
space_c=0
sp_c=0
dict ={}
for i in n:
    if i.isalpha():
        alpha_c+=1
    elif i.isdigit():
        digi_c+=1
    elif i in sp:
        sp_c+=1
    if i == " ":
        space_c+=1
dict.setdefault("alphabets_count",alpha_c)
dict.setdefault("digits_count",digi_c)
dict.setdefault("special characters",sp_c)
dict.setdefault("space_count",space_c)
print(f"dictionary :{dict}")