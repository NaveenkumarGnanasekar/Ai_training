n1=set(input("enter the movies watched by person1 with(,):").split(","))
n2 = set(input("enter the movies watched by person2 with(,):").split(","))
print(f"the movies watched by both :{n1.intersection(n2)}")
print(f"the movies watched by either one:{n1.symmetric_difference(n2)}")