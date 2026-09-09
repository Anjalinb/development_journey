arr=[10,1,15,11,16,10,11,12,90,15,10,1]
arr_set=set(arr)
num_count={}
for num in arr_set:
    num_count[num]=arr.count(num)

print(num_count)
