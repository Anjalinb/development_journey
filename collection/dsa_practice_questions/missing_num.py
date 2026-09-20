arr=[1,3,4,6,2]
arr.sort()
i=1
for num in arr:
    
    if num+1!=arr[i]:
        print(num+1)
        break
    i+=1