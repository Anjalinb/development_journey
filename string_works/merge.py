"""
word1="ABC"
word2="PQR"
merged_str=APBQCR

"""

word1="ABCD"
word2="PQRS"
merged_str=""
for i in range(0,len(word1)):
    merged_str+=word1[i]+word2[i]
print(merged_str)
