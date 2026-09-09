
from mysql import connector

class ExpenseListCreateRetreiveUpdateDelete:
    
    def __init__(self,user=None,password=None):
        self.connection=connector.connect(
             user=user,
                password=password,
                host='localhost',
                database='tripwise_db'
        )

        self.cursor=self.connection.cursor()

    def post(self,**kwargs):

        query="""
        insert into expense(trip,paid_by,amount,category) values(%s,%s,%s,%s)
        """
        values=list(kwargs.values())
        self.cursor.execute(query,values)
        self.connection.commit()
        print("record has been added")

    def get(self):
        query="select * from expense"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        for exp in records:
            print(exp)

    def retrieve(self,id=None):
        query="select * from expense where id=%s"
        values=(id,)
        self.cursor.execute(query,values)
        records=self.cursor.fetchall()
        print(records)

    def put(self,id=None,**kwargs):

        placeholder=""
        for k in kwargs.keys():
            placeholder += k+"=%s,"
        placeholder=placeholder.rstrip(",")

        query=f"update expense set {placeholder} where id=%s"
        values=list(kwargs.values())
        values.append(id)
        self.cursor.execute(query,values)
        self.connection.commit()
        print("record has been updated")
        





exp_instance=ExpenseListCreateRetreiveUpdateDelete(user="root",password="root")
print(exp_instance.connection)

#exp_instance.post(trip="kerala-manali",paid_by="ajna menon",amount=5000,category="ticket")
# exp_instance.get()
#exp_instance.retrieve(2)
exp_instance.put(id=2,amount=500,paid_by='sajna menon',category="food")