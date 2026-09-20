words=["silent","listen","act","cat","note","tone","hen","chicken"]
anagrams=[]
for w1 in words:
    for w2 in words:
     
        if sorted(w1)==sorted(w2) and w2!=w1:
            anagrams.append(w1)
         

print(anagrams)


        
        