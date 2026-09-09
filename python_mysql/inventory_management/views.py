from mysql import connector

class ProductListCreateRetreiveUpdateDelete:

    def __init__(self,user=None,password=None):
        if user==None or password==None:
            raise Exception("username and password required")

        self.connection=connector.connect(
            user=user,
            password=password,
            host="localhost",
            database="inventory_db"
        )

        self.cursor=self.connection.cursor()

    def post(self,**kwargs):
        db_cols=("product_name","category","quantity","reorder_level","unit_price","supplier","status")
        difference=set(db_cols).difference(kwargs.keys())
        if difference:
            raise Exception(f"{difference} required")

        col_str=",".join(db_cols)

        query=f"insert into products ({col_str}) values(%s,%s,%s,%s,%s,%s,%s)"
        values=list(kwargs.values())
        self.cursor.execute(query,values)
        self.connection.commit()
        print("record has been inserted")

    def get(self):
        query="select * from products"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        for r in records:
            print(r)

    def retrieve(self,id=None):
        query="select * from products where id=%s"
        values=(id,)
        self.cursor.execute(query,values)
        records=self.cursor.fetchone()
        print(records)

    def put(self,id=None,**kwargs):
        placeholder=""
        for k in kwargs.keys():
            placeholder+= k+"=%s,"
        placeholder=placeholder.rstrip(",")

        query=f"update products set {placeholder} where id=%s"
        values=list(kwargs.values())
        values.append(id)
        self.cursor.execute(query,values)
        self.connection.commit()
        print("record has been updated")

    def delete(self,id=None):
        query="delete from products where id=%s"
        values=(id,)
        self.cursor.execute(query,values)
        self.connection.commit()
        print("record has been deleted")

    def filter(self,**kwargs):
        placeholder=""
        for k in kwargs.keys():
            placeholder+= k+"=%s and "
        placeholder=placeholder.rstrip("and ")
        query=f"select * from products where {placeholder}"
        values=list(kwargs.values())
        self.cursor.execute(query,values)
        records=self.cursor.fetchall()
        if records:
            for r in records:
                print(r)
        else:
            print("no records")

    def summary(self):
        query="select status,count(*) from products group by status"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        print(records)





product=ProductListCreateRetreiveUpdateDelete(user="root",password="root")
# print(product.connection)

# product.post(
#     product_name="Laptop",
#     category="Electronics",
#     quantity=25,
#     reorder_level=10,
#     unit_price=55000.00,
#     supplier="Dell",
#     status="in_stock"
# )

# product.post(
#     product_name="Wireless Mouse",
#     category="Accessories",
#     quantity=8,
#     reorder_level=10,
#     unit_price=750.00,
#     supplier="Logitech",
#     status="low_stock"
# )

# product.post(
#     product_name="Keyboard",
#     category="Accessories",
#     quantity=15,
#     reorder_level=5,
#     unit_price=1200.00,
#     supplier="HP",
#     status="in_stock"
# )

# product.post(
#     product_name="USB Cable",
#     category="Accessories",
#     quantity=0,
#     reorder_level=10,
#     unit_price=300.00,
#     supplier="Portronics",
#     status="out_of_stock"
# )

# product.post(
#     product_name="Printer Ink",
#     category="Office Supplies",
#     quantity=4,
#     reorder_level=5,
#     unit_price=1800.00,
#     supplier="Canon",
#     status="low_stock"
# )

# product.get()
# product.retrieve(5)
# product.put(id=5,quantity=3,unit_price=1900.00)
# product.delete(5)
# product.filter(status="out_of_stock",supplier="portronics")
product.summary()