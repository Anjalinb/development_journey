word="pneumonoultramicroscopicsilicovolcanoconiosis"
v_count=0
c_count=0
for ch in word:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            v_count+=1
        else:
            c_count+=1

print("Vowel count=",v_count)
print("Consonant count=",c_count)