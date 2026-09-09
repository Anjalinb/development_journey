sales=[100000,120000,110000,115000,90000,70000]
march_month_sales=sales[2]
print(march_month_sales)
print("\n")
sales[4]=105000

for i in range(0,len(sales)):
    print(sales[i])

print("Sales greater than 100000:")

for amount in sales:
    if amount>100000:
        print(amount)