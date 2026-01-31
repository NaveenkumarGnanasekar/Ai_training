days = int(input ("enter the number of days :"))
years = days // 365
weeks = (days) // 7
remaining_days = (days) % 7
print(years,"years",weeks,"weeks",remaining_days,"days")
print (days % 365)