arr=[3,7,4,9,10,11,12,13]
prime=list()
for num in arr:
    for i in range(2,num):
        if num%i==0:
            break
    else:
        prime.append(num)


print(prime)