n = int(input("enter the number of customers:"))
dict={}
for i in range(1,n+1):
    customer=input("enter customer's name :")
    total_amount = int(input("enter the total amount :"))
    dict[customer]=total_amount
for i,j in dict.items():
    discount = 0 
    if j >= 5000 and j <=10000:
        discount = 0.10 * j
        j = j - discount
        dict[i]=j
    elif j >10000:
        discount=0.20*j
        j = j -discount
        dict[i]=j
print(f"final dictionary with discount = {dict}")