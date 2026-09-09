text="hello world"

text_count=text.count("hell")#gives frequency of value

print(text_count)

print(text.find("l"))# gives index of first occurence, retuens -1 if no occurence

print(text.find("x"))

print(text.rfind("l"))#gives index of last occurence

print(text.index("l"))#gives index, return error if no occurence

print(text.startswith("he"))#checks if the string starts with substring

print(text.endswith("orld"))#checks if the string ends with substring

new_txt=text.replace("world","there")

print(new_txt)
