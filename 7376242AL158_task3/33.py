r={"python","ros","c++","opencv","ml"}
s=set(input("enter student skills:").split())
print(f"missing skills :{r.difference(s)}")
print(f"extra skills:{s.difference(r)}")