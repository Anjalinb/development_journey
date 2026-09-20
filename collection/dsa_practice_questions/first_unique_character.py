"""
reutrn the index of first unique char. return -1 if no unique char
"""

text="abcabc"
for i in text:
    if text.count(i)==1:
        print(text.find(i))
        break
else:
    print("-1")