words=['silent','listen','race','care','trap','night','tight']
fw=open("file_operations\\anagrams.txt",'w')
for w1 in words:
    for w2 in words:
       
        if sorted(w1)==sorted(w2) and w2!=w1:
            fw.write(w1+"\n")
            

