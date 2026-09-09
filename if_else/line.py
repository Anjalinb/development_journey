x1=int(input("Enter x coordinate for point 1:"))
y1=int(input("Enter y coordinate for point 1:"))
x2=int(input("Enter x coordinate for point 2:"))
y2=int(input("Enter y coordinate for point 2:"))
x3=int(input("Enter x coordinate for point 3:"))
y3=int(input("Enter y coordinate for point 3:"))
slope1=(y2-y1)/(x2-x1)
slope2=(y3-y2)/(x3-x2)
if slope1==slope2:
    print("The points form a straight line")
else:
    print("The points do not form a straight line")