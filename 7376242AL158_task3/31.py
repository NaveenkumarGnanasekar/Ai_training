sentence1 = set(input("enter sentence:").lower().split())

sentence2 = set(input("enter sentence 2:").lower().split())
sentence3 = set(input("enter sentence 3").lower().split())
print(f"common words in the given sentence = {sentence1.intersection(sentence2,sentence3)}")