num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
option=input("Enter the choice min or max:")
match option:
    case "min":
        print("Minimum is",min(num1,num2))
    case "max":
        print("Maximum is",max(num1,num2))
    case _: print("Invalid input")