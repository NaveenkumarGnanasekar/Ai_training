n = list (map(int,input("enter a list:").split()))
even_list = [x for x in n if x%2==0]
odd_list = [x for x in n if x%2!=0]
print(f"list with even numbers :{even_list}")
print(f"list with odd numbers:{odd_list}")
