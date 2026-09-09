year=int(input("Enter the year:"))
is_div=(year%100!=0 and year%4==0) or (year%100==0 and year%400==0)
print(is_div)