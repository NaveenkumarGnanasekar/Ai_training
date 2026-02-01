late = int(input ("enter time :"))
penalty = 0 
if late <= 10 :
    penalty = 0 
elif late >10 and late <= 30 :
    penalty = 50 
else :
    penalty = 100
print(" penalty amount  =", penalty )
