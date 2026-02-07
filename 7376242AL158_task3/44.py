sentence = input("enter a sentence:")
w = sentence.split()
dict = {}
for i in range(len(w) - 1):
    pair = (w[i], w[i+1])
    dict[pair] = dict.get(pair, 0) + 1
print(dict)
