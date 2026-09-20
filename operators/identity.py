""" identity operator: chks if two variables are pointing to same location or not
"""

p1="anjali"
p2="anjali"
print(p1==p2)
print(p1 is p2)

p1_food=["burger","fries"]
p2_food=["burger","fries"]
print(p1_food==p2_food)
print(p1_food is p2_food)

a={"a":1,"b":2}
b={"a":1,"b":2}
print(a==b)
print(a is b)

a1=(1,2,3)
a2=(1,2,3)
print(a1 is a2)

