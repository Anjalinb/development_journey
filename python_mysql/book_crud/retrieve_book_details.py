from mysql import connector

connection=connector.connect(
    user="root",
    password="root",
    host="localhost",
    database="book_db"
)
cursor=connection.cursor()

query="""
select * from book where id=%s
"""
values=(2,)

cursor.execute(query,values)
records=cursor.fetchone()
print(records)