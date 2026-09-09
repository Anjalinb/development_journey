class Shape:
    name:str
    def __init__(self,name):
        self.name=name

class Parallelogram(Shape):
    base=int
    height=int
    def __init__(self,name,base,height):
        super().__init__(name)
        self.base=base
        self.height=height
    def area(self):
        print("Area of",self.name,"is",self.base*self.height)

parallelogram_instance=Parallelogram("Parallelogram",12,14)
parallelogram_instance.area()

class Rectangle(Shape):
    length:int
    width:int
    def __init__(self,name,length,width):
        super().__init__(name)
        self.length=length
        self.width=width

    def area(self):
        print("Area of",self.name,"is",self.length*self.width)

rec_instance=Rectangle("rectangle",12,14)
rec_instance.area()


class Circle(Shape):
    radius:int
    def __init__(self,name,radius):
        super().__init__(name)
        self.radius=radius
    def area(self):
        print("Area of",self.name,"is",3.14*(self.radius**2))

cr_instance=Circle("circle",7)
cr_instance.area()


class Trapezium(Shape):
    side1:int
    side2:int
    height:int
    def __init__(self,name,side1,side2,height):
        super().__init__(name)
        self.side1=side1
        self.side2=side2
        self.height=height
    def area(self):
        print("Area of",self.name,"is",((self.side1+self.side2)*self.height)/2)

tr_instance=Trapezium("trapezium",4,8,7)
tr_instance.area()



