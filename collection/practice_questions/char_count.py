word="python programming is simple"
word_set=set(word)
char_count={}
for w in word_set:
    char_count[w]=word.count(w)

print(char_count)