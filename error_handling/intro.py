"""
try- doubtful code
except- handling errors
finally- clean up process
raise- throw custom errors
assert-debugging
"""



num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
try:
    result=num1/num2
    print("result",result)
except Exception as e:
    print(e)
print("db transaction")
print("file writing")