lst=[2,3,4,56,76,78,54,77,12,13,31]
new=[3,67,32,-98,-54,-23]
print("Even numbers:")
for num in lst:
    if num%2==0:
        print(num)

print("Odd numbers:")
for num in lst:
    if num%2!=0:
        print(num)

print("Numbers greater than 50:")
for num in lst:
    if num>50:
        print(num)

print("Numbers smaller than 20:")
for num in lst:
    if num<20:
        print(num)

print("Prime numbers:")
for num in lst:
    for i in range(2,num):
        if num%i==0:
            break
    else:
        print(num)

print("Negative numbers:")
for num in new:
    if num<0:
        print(num)