atm_pin=5432
for i in range(1,4):
    pin=int(input("Enter the PIN:"))
    if pin==atm_pin:
        print("Unlocked")
        break
    
   
else:
    print("Blocked")

# 