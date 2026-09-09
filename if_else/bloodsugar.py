"""
### 1. Blood Sugar
- < 100: Normal
- 100 - 125: Prediabetes
- ≥ 126: Diabetes
"""
bld=int(input("enter blood sugar level="))

if bld<100:

    print("NORMAL")

elif bld>=100 and bld<=125:

    print("prediabetes")

else:

    print("diabetes")