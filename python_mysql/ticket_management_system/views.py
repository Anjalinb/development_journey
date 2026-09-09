from mysql import connector

class TicketListCreateRetreiveUpdateDelete:

    def __init__(self,user=None,password=None):
        if user==None or password==None:
            raise Exception("username and password required")

        self.connection=connector.connect(
            user=user,
            password=password,
            host="localhost",
            database="customer_support_db"
        )

        self.cursor=self.connection.cursor()

    def post(self,**kwargs):
        db_cols=("customername","email","subject","description","category","priority","status","assignedto")

        difference=set(db_cols).difference(kwargs.keys())
        if difference:
            raise Exception(f"{difference} required")
        
        col_str=",".join(db_cols)
        
        query=f"insert into supportticket ({col_str}) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        values=list(kwargs.values())
        self.cursor.execute(query,values)
        self.connection.commit()
        print("record has been inserted")

    def get(self):
        query="select * from supportticket"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        for ticket in records:
            print(ticket)

    def retrieve(self,id=None):
        query="select * from supportticket where id=%s"
        values=(id,)
        self.cursor.execute(query,values)
        records=self.cursor.fetchone()
        print(records)

    def put(self,id=None,**kwargs):
        placeholder=""
        for k in kwargs.keys():
            placeholder+= k+"=%s,"
        placeholder=placeholder.rstrip(",")

        query=f"update supportticket set {placeholder} where id=%s"
        values=list(kwargs.values())
        values.append(id)
        self.cursor.execute(query,values)
        self.connection.commit()
        print("record has been updated")

    def delete(self,id=None):
        query="delete from supportticket where id=%s"
        values=(id,)
        self.cursor.execute(query,values)
        self.connection.commit()
        print("record has been deleted")

    def filter(self,**kwargs):

        placeholder=""
        for k in kwargs.keys():
            placeholder+= k+"=%s and "
        placeholder=placeholder.rstrip("and ")

        query=f"select * from supportticket where {placeholder}"
        values=list(kwargs.values())
        self.cursor.execute(query,values)
        records=self.cursor.fetchall()
        if records:
            for r in records:
                print(r)
        else:
            print("No records")

    def summary(self):
        query="select status,count(*) from supportticket group by status"
        self.cursor.execute(query)
        response=self.cursor.fetchall()
        priority_query="select priority,count(*) from supportticket group by priority"
        self.cursor.execute(priority_query)
        priority_summary=self.cursor.fetchall()

        print("priority summary:",priority_summary)
        print(response)





ticket=TicketListCreateRetreiveUpdateDelete(user="root",password="root")
# print(ticket.connection)
ticket.post(customername="Ananya",
email="ananya@gmail.com",
subject="Unable to login",
description="I am unable to log in to my account even though my password is correct.",
category="account",
priority="medium",
status="inprogress",
assignedto="Sneha")

# ticket.get()

# ticket.retrieve(id=4)

# ticket.put(id=2,customername="sajna",email="sajna@gmail.com")

# ticket.delete(id=6)
# ticket.filter(category="payment",priority="medium")
# ticket.summary()

