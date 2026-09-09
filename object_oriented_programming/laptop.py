class Laptop:
    brand:str
    color:str
    storage:int
    price:int

    def __init__(self,brand,color,storage,price):
        self.brand=brand
        self.color=color
        self.storage=storage
        self.price=price

    def get_laptop(self):
        print(self.brand,self.color,self.storage,self.price)

  


hp_instance=Laptop("hp","black",123,40000)


hp_instance.get_laptop()
    

