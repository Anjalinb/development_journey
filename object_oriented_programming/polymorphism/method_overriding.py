"""
METHOD OVERRIDING
child class redefine the method that is already defined in parent class

"""

class Parent:
    def mobile(self):
        print("redmi note 14")

class Child(Parent):
    def mobile(self):
        print("Iphone 16")

ch_instance=Child()
ch_instance.mobile()