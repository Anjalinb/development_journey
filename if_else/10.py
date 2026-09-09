n=int(input("Enter the number:"))
if n%100==0 and n%400==0:
    print(n,"is divisible by 100 and 400")
else:
    print(n,"is not divisible by 100 and 400")