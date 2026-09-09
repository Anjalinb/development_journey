"""
oop = a way of programming to convert real world entities to programs using class and object
class-plan, design pattern, template, bluepri
nt for creating an object
object= real world entity created using class

CONSTRUCTOR
-used to initialize attributes
name of constructor will be __init__
automatically called while creating object of a class

"""

class Animal:
    name:str
    sound:str

    def walk(self):
        print("animal is walking")

    def sleep(self):
        print("animal is sleeping")

cat_instance=Animal()
dog_instance=Animal()
cat_instance.walk()
dog_instance.sleep()