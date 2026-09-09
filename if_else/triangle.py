angle1=int(input("Enter angle 1:"))

angle2=int(input("Enter angle 2:"))

angle3=int(input("Enter angle 3:"))

sum=angle1+angle2+angle3

if angle1>0 and angle2>0 and angle3>0:
    if sum==180:
        print("It is a triangle")
    else:
        print("Cannot form a triangle")
else:

    print("Angles should be greater than 0")
