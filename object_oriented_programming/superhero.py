class Superhero:
    name:str
    power:str
    universe:str

    def set_superhero(self,name,power,universe):
        self.name=name
        self.power=power
        self.universe=universe

    def get_superhero(self):
        print(self.name,self.power,self.universe)

superhero_instance1=Superhero()
superhero_instance1.set_superhero("spiderman","web","marvel")
superhero_instance2=Superhero()
superhero_instance2.set_superhero("batman","rich","dc")
superhero_instance3=Superhero()
superhero_instance3.set_superhero("Minnal murali","run","basil")

superhero_instance1.get_superhero()
superhero_instance2.get_superhero()
superhero_instance3.get_superhero()
