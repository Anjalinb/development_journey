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