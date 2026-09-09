def is_anagram(word1,word2):
    word1=word1.lower()
    word2=word2.lower()
    for ch in word1:
        if ch not in word2 or word1.count(ch)!=word2.count(ch):
            print(False)
            break
    else:
        print(True)

is_anagram("silents","listen")
is_anagram("silEnts","listens")
