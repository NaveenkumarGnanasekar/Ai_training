ch = [chr(i) for i in range(ord("a"),ord("z")+1)]
n = input("enter a sentence:").lower()
for i in n:
    if i in ch:
        ch.remove(i)
    else:
        continue
if ch ==[]:
    print("the given sentence is a panagram")
else:
    print("the given sentence is not a panagram")