n = int(input("enter number of device:"))
dict = {}
for i in range(1,n+1):
    device_id = int(input("enter the device id :"))
    lst = list(input("enter status log of device :").lower().split())
    dict[device_id]=lst
for i,j in dict.items():
    if "off" in j :
        print("device",i,"was Offed")
    else:
        print("device",i , "were always ON")