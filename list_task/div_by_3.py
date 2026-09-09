lst=[1,4,6,9,12,24]
for num in lst:
    if num%3==0:
        print(num)

print("No of elements:",len(lst))
print("Largest element:",max(lst))
print("Smallest element:",min(lst))
print("Sum of elements:",sum(lst))
print("Average of elements:",sum(lst)/len(lst))