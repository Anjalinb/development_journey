note="hene"
magazine="chicken"
for char in note:
    if char not in magazine:
        print("Not ransome note")
        break
else:
    print("Ransome note")