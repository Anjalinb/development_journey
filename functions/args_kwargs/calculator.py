def calculator(*args,operation):
    if operation=="+":
        return sum(args)
    elif operation=="*":
        product=1
        for num in args:
            product=product*num
        return product

print(calculator(10,20,30,operation="+"))
print(calculator(10,20,30,operation="*"))

#METHOD 2

def calculator(*args,**kwargs):
    if kwargs.get("operation")=="+":
        return sum(args)
    elif kwargs.get("operation")=="*":
        product=1
        for num in args:
            product=product*num
        return product

print(calculator(10,20,30,operation="+"))
print(calculator(10,20,30,operation="*"))

