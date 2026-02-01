balance = int(input ("enter balance in account :"))
interest = 0
if balance < 10000:
    interest = (balance * 0.03) / 12
elif balance >=10000 and balance <=50000:
    interest = (balance * 0.05) / 12

else :
    interest = (balance * 0.07) / 12
print("enter monthy interest amount = ", interest ) 