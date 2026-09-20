words=["madam","tan",'ant','racecar','malayalam']
palindrome_words=[]
for word in words:
    if word==word[::-1]:
        palindrome_words.append(word)
        
print(palindrome_words)