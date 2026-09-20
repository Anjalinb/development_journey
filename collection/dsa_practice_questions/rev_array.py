"""
reverse a list without using reverse() and slicing

"""
arr=[1,2,3,4]
new=[]
for i in range(len(arr)-1,-1,-1):
    new.append(arr[i])
print(new)
