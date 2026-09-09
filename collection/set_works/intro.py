"""
define={value}  (there should be atleast one value, otherwise considered as dict)
order not preserved (random order)
METHODS

add(value): adds value to random position
union(set)
intersection(set)
difference(set)
issuperset(set)
issubset(set)
"""
st={}
print(type(st))  #dict
st={10,40,20,20,10,56,1}
st.add(456)
print(st)

set1={10,20,30,40}
set2={10,20,100,200,300}

union_set=set1.union(set2)
print("Union set=",union_set)

inter_set=set1.intersection(set2)
print("Inersection set=",inter_set)

diff_set1=set1.difference(set2) #removes elements of set2 from set1
diff_set2=set2.difference(set1) #removes elements of set1 from set2

print("set1-set2=",diff_set1)
print("set2-set1=",diff_set2)

s1={10,20,30,80,90}
s2={10,30,80}
print(s1.issuperset(s2))
print(s2.issubset(s1))

note="hene"
magazine="chicken"
print(set(note).issubset(magazine))