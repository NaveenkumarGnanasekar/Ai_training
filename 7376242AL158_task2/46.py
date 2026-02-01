access = 3
pin = 1234
for i in range (access,0,-1):
    user = int(input("enter pin :"))
    if pin == user :
        print("access granted ")

        break
    else :
        print(f"invalid pin, {i-1} remaining attempts")
        continue
else :
    print("card blocked ")
    