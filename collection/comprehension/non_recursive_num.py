arr=[10,11,1,10,11,2,3]

non_recursive=[num for num in arr if arr.count(num)==1]
print(non_recursive)

duplicate={num for num in arr if arr.count(num)>1}
print(duplicate)