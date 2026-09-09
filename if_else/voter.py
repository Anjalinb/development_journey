age=int(input("Enter age:"))
if age>=18:
    chk=input("Did you pass the test(y/n):")
    if chk=="y":
        print("License approved")
    else:
        print("Test not cleared")
else:
    print("Not eligible due to age")