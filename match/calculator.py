num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
choice=input("Enter the operator (+,-,*,/):")
match choice:
    case "+":
        print(num1,"+",num2,"=",num1+num2)
    case "-":
        print(num1,"-",num2,"=",num1-num2)
    case "*":
        print(num1,"*",num2,"=",num1*num2)
    case "/":
        print(num1,"/",num2,"=",num1/num2)
    case _:
        print("Invalid input")
        