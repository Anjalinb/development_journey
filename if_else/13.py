n=int(input("Enter the year:"))
if n%100!=0 and n%4==0:
    print(n,"is not divisible by 100 and divisible by 4")
else:
    print(n,"is not")