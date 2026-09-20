"""
A kangaroo word is a word that contains another word inside it,
 with the letters of the smaller word appearing in the same order, usually with some letters in between.
 Eg:
 MASCULINE
 MALE
"""
big=input("Enter bigger word:")
small=input("Enter smaller word:")

j=0

for ch in big:
    if j<len(small) and ch==small[j]:
        j+=1

if j==len(small):
    print("Kangaroo word")
else:
    print("Not a kangaroo word")