text="hello$world#"
vowels=[]
consonants=[]
specials=[]
for ch in text:
    if ch.lower() in "aeiou":
        vowels.append(ch)
    elif ch.isalpha():
        consonants.append(ch)
    else:
        specials.append(ch)

print("Vowels=",vowels)
print("Consonants=",consonants)
print("Special characters=",specials)