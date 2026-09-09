"""
define={key:value}
mutable:yes
duplicates: duplicate key not allowed

METHODS
keys() - return all keys
values()- return all values
items() - return all key and value
get(key) - gives value of the key, gives none if key doesn't exist

"""

daily_calories={"mon":1200,"tue":2000,"wed":5000,"thurs":1200,"fri":3200,"sat":5000,"sun":4050,"mon":1300} 
# if duplicate key given, takes the second value
print(daily_calories)
print(daily_calories["wed"])

daily_calories["fri"]=3250
print(daily_calories)

print("All keys--")
for k in daily_calories.keys():
    print(k)

print("All values--")
for v in daily_calories.values():
    print(v)

print("Keys and values--")
for k,v in daily_calories.items():
    print(k,v)

print(daily_calories.get("total")) # gives none if key doesn't exist
print(daily_calories.get("total",0)) # gives 0 if key doesn't exist
#print(daily_calories["total"])     # gives error if key doesn't exist

daily_calories["total_cal"]=sum(daily_calories.values())
print(daily_calories)
