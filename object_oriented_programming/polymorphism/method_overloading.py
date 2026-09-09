"""
polymorphism- many forms
-method overloading: same method name, different no of parameters (not supported in python)


"""

class Calculator:

    def add(self,num1,num2):
        print(num1+num2)

    def add(self,num1,num2,num3):
        print(num1+num2+num3)

    def add(self,num1,num2,num3,num4):
        print(num1+num2+num3+num4)

cl_instance=Calculator()
cl_instance.add(1,2,3,4)
cl_instance(1,2) #error, only remembers the last defined method
