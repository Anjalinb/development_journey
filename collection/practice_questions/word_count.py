words=["hai","hello","hai","hai","hai"]
words_set=set(words)
word_count={}
for w in words_set:
    word_count[w]=words.count(w)

print(word_count)