word1="silents"
word2="listen"
c1=len(word1)
c2=len(word2)

for ch in word1:
    if ch not in word2 or word1.count(ch)!=word2.count(ch):
        print("Not anagram")
        break
else:
    print("Anagram")







        

   
    