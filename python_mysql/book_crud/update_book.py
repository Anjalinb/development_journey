from mysql import connector

connection=connector.connect(
    user="root",
    password="root",
    host="localhost",
    database="book_db"
)
cursor=connection.cursor()

query="""
update book set pages=%s where id=%s
"""

values=(450,3)
cursor.execute(query,values)
connection.commit()
print("record has been updated")