class Employee:
    id:int
    name:str
    salary:int
    phone:int
    dept:str

    def __init__(self,id,name,salary,phone,dept):
        self.id=id
        self.name=name
        self.salary=salary
        self.phone=phone
        self.dept=dept
    def get_employee(self):
        print(self.id,self.name,self.salary,self.phone,self.dept)

emp1_instance=Employee(1,"anj",100000,8976546688,"hr")

emp1_instance.get_employee()