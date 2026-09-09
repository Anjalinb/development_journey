arr=[10,1,15,16,11,10,12,11]
duplicate_num=set()
for num in arr:
    if arr.count(num)>1:
        duplicate_num.add(num)

print(duplicate_num)