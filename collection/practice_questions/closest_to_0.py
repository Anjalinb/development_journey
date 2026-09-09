arr=[-3,-2,-1,2,3,4]
smallest_difference=abs(arr[0]-0)
for num in arr:
    difference=abs(num-0)
    if difference<smallest_difference:
        smallest_difference=difference
        result=num

print(result)


