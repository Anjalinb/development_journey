n=int(input("Enter the year:"))
if (n%100!=0 and n%4==0) or (n%100==0 and n%400==0):
    print(n,"is a leap year")
else:
    print(n,"is not a leap year")