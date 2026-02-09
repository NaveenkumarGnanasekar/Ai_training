n = int(input("Enter number of cities: "))
aqi = {}
for _ in range(n):
    city = input("City: ")
    values = list(map(int, input("Daily AQI values: ").split()))
    aqi[city] = values
avg_aqi = {}
for city, values in aqi.items():
    avg_aqi[city] = sum(values) / len(values)
worst_city = max(avg_aqi, key=avg_aqi.get)
print("Average AQI per city:", avg_aqi)
print("City with worst average AQI:", worst_city, "(", avg_aqi[worst_city], ")")