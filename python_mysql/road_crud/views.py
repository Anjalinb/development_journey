from mysql import connector

class IssueListCreateRetreiveUpdateDelete:

    def __init__(self,user=None,password=None):
        self.connection=connector.connect(
            user=user,
            password=password,
            host="localhost",
            database="road_issue_db"
        )

        self.cursor=self.connection.cursor()

    def post(self,**kwargs):
        query="insert into issues(title,location,posted_by,status) values(%s,%s,%s,%s)"
        values=list(kwargs.values())
        self.cursor.execute(query,values)
        self.connection.commit()
        print("record has been added")

    def get(self):
        query="select * from issues"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        for i in records:
            print(i)

    def retrieve(self,id=None):
        query="select * from issues where id=%s"
        values=(id,)
        self.cursor.execute(query,values)
        records=self.cursor.fetchone()
        print(records)

    def put(self,id=None,**kwargs):
        placeholder=""
        for k in kwargs.keys():
            placeholder+= k+"=%s,"
        placeholder=placeholder.rstrip(",")

        query=f"update issues set {placeholder} where id=%s"
        values=list(kwargs.values())
        values.append(id)
        self.cursor.execute(query,values)
        self.connection.commit()
        print("record has been updated")

    def delete(self,id=None):
        query="delete from issues where id=%s"
        values=(id,)
        self.cursor.execute(query,values)
        self.connection.commit()
        print("record has been deleted")





road_instance=IssueListCreateRetreiveUpdateDelete(user="root",password="root")
# print(road_instance.connection)

# road_instance.post(title="rutting",location="rs street",posted_by="arun",status="unsolved")
# road_instance.get()
# road_instance.retrieve(id=3)
# road_instance.put(id=3,posted_by="shyam",status="solved")
road_instance.delete(id=3)