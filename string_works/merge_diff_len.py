word1="ABC"
word2="PQRSTU"
merged_str=""
small_str=""
large_str=""
if len(word1)<len(word2):
    small_str=word1
    large_str=word2
else:
    small_str=word2
    large_str=word1

for i in range(0,len(small_str)):
    merged_str+=word1[i]+word2[i]

merged_str+=large_str[len(small_str):]
print(merged_str)
