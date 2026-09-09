text="the quick brown fox jumps over lazy dog"
alphabets="abcdefghijklmnopqrstuvwxyz"
for char in alphabets:
    if char not in text:
        print("Not pangram")
        break
else:
    print("Pangram")