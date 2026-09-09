"""
### 2. Blood Pressure (Systolic)
- < 120: Normal
- 120 – 129: Elevated
- 130 – 139: High BP Stage 1
- ≥ 140: High BP Stage 2

"""
bld_press=int(input("enter blood pressure"))

if bld_press<120:

    print("normal")

elif bld_press>=120 and bld_press<=129:

    print("elevated")

elif bld_press>=130 and bld_press<=139:

    print("high bp stage 1")

else:

    print("high bp satge 2")