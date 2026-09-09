age=[("John",18),("Alice",22),("Bob",16),("Emma",25)] 
age_dict=dict(age)
print(age_dict)
new=[k for k,v in age_dict.items() if v>18]
print(new)