a = list(map(int, input("enter list 1 : ").split()))
b = list(map(int, input("enter list 2 : ").split()))
if len(a) != len(b):
    print("false")
else:
    if b in (a + a):
        print("true")
    else:
        print("false")
