year = int(input ("enter the year of serivce :"))
bonus =0 
if year < 2 :
    bonus =0
elif year >=2 and year <=5:
    bonus=5000
elif year >=6 and year <=10:
    bonus=10000
else :
    bonus = 20000
print("bonus amount = ", bonus)