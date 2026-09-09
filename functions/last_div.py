number=int(input("Enter the number:"))
for i in range(1,number):
    if number%i==0:
        last_div=i
print(last_div)