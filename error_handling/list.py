lst=[10,11,12,13,14,15]
index=int(input("Enter index position:"))
try:
    print(lst[index])
except Exception as e:
    print(e)

print("db transaction")
print("file writing")