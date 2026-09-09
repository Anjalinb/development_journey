num1=int(input("Enter number1:"))
num2=int(input("Enter number2:"))

operation=input("Select operation + - * /")
result=0
try:
    if operation=="+":
        result=num1+num2
    elif operation=="-":
        result=num1-num2
    elif operation=="*":
            result=num1*num2
    elif operation=="/":
            result=num1/num2
    else:
        print("Invalid operation")
except Exception as e:
    print(e)
else:
     print(result)