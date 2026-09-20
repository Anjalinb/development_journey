arr=[-3,-2,-1,1,2,3,4]
closest=arr[0]
for num in arr:
    if abs(num)<abs(closest):
        closest=num

if closest<0 and abs(closest) in arr:
    print(abs(closest))
else:
    print(closest)



