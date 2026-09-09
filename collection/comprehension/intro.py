"""
comprehension- easy way of creating a collection from a sequence

SYNTAX

list comprehension = [value iteration condition]
set comprehension = {value iteration condition}
dictionary comprehension = {key:value iteration condition}

"""
arr=[2,3,4,5,6]
squares=[num**2 for num in arr]
print(squares)

add_ten=[num+5 for num in arr]
print(add_ten)

cubes=[num**3 for num in arr]
print(cubes)

evens=[num for num in arr if num%2==0]
print(evens)

odds=[num for num in arr if num%2!=0]
print(odds)

num_gt_5=[num for num in arr if num>5]
print(num_gt_5)