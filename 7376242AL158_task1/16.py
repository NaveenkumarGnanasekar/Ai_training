char = input("enter a character :")
special_characters = ['@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '!', '~', '`', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/',' ']
if char.isalpha():
    print(char , "is an alphabet")
elif char.isdigit():
    print(char , "is a digit")
elif char in special_characters:
    print(char , "is a special character")
else :
    print("unknown character type")