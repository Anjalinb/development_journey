text="a man a canal panama"
consonants={ch for ch in text if ch not in "aeiou" and ch.isalpha()}
print(consonants)