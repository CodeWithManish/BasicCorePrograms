string = "Hello <<UserName>>, How are you?"
input = input("Enter Name: ")
value = string.replace("<<UserName>>", input)
print(value)