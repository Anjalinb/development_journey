arr=[10,1,15,16,11,10,12,11,12,18,12]
most_freq=arr[0]
for num in arr:
    if arr.count(num)>arr.count(most_freq):
        
        most_freq=num


print(most_freq)
