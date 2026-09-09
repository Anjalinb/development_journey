"""
slicing = extracting a portion from a sequence
"""

text="A man, a plan, a canal Panama"
#     0123456789012345678901234567890
#               1         2  
substr=text[17:22]
print(substr)
substr1=text[9:13]
print(substr1)
substr2=text[23:]
print(substr2)
substr3=text[:5]
print(substr3)
copy=text[:]
print(copy)