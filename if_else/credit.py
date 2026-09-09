cr=int(input("Enter credit score:"))
if (cr>=800 and cr<=850):
    print("Excellent")
elif(cr>=740 and cr<=799):
    print("Very good")
elif(cr>=670 and cr<=739):
    print("good")
elif(cr>=580 and cr<=669):
    print("Fair")
else:
    print("Poor")
