hcm=int(input("Enter height in cm: "))
weight=int(input("Enter weight in kg:"))
hm=hcm/100
bmi=weight/hm**2
print("BMI:",bmi)
if bmi<19: print("Underweight")
elif bmi>19 and bmi<=25: print("Normal")
elif bmi>25 and bmi<=30: print("Overweight")
else: print("Obese")