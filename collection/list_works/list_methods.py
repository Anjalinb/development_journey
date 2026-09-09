
"""
ADD:
append(value)= add object at end of list
insert(value,index)= inserts value at specific index

REMOVE:
pop(index): removes object from specific index, default index=-1
remove(value): removes first ocuurence of object

index(value)= returns index of first occurence of value
count(value)= returns frequency of value
reverse()= reverse the list
sort()= sorts the list
copy()= creates a copy of the list. but it will point to a different object

"""


colors=["red","green","blue","red","violet","blue"]

colors.append("white")
print(colors)

colors.insert(3,"orange")
print(colors)

colors.pop(1)
print(colors)

colors.remove("red")
print(colors)

print(colors.index("white"))

print(colors.count("blue"))

colors.reverse()
print(colors)

colors.sort()
print(colors)
colors.sort(reverse=True) #descending order
print(colors)

new_clr=colors.copy()
new_clr[0]="brown" #change will not effect original list
print(colors)
print(new_clr)