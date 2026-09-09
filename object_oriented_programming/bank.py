class Bank:
    acc_number=int
    balance:int
    acc_type:str
    customer_name:str

    def __init__(self,acc_number,balance,acc_type,customer_name):
        self.acc_number=acc_number
        self.balance=balance
        self.acc_type=acc_type
        self.customer_name=customer_name
        print("Account created")

    def deposit(self,amount):
        self.balance+=amount
        print(f"Your {self.acc_number} has been credited with {amount}. available balance is {self.balance} ")

    def withdraw(self,amount):
        if self.balance<amount:
            raise Exception("Insufficient balance")
        else:
            self.balance-=amount
            print(f"Your {self.acc_number} has been debited with {amount}. available balance is {self.balance} ")

    def get_balance(self):
        print(f"Available balance is {self.balance}")

c1_instance=Bank(537386,500,"savings","anj")

c1_instance.deposit(1000)
c1_instance.withdraw(500)
c1_instance.get_balance()



