expenses=[12000,23000,30000,12000,15000,20000]
march_month_exp=expenses[2]
print(march_month_exp)

expenses[0]=15000
print(expenses)

print("using index===")
for i in range(0,len(expenses)):
    print(expenses[i])

print("using in===")
for amount in expenses:
    print(amount)
    