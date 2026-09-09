from mysql import connector

connection=connector.connect(
    user="root",
    password="root",
    host="localhost",
    database="book_db"
)
cursor=connection.cursor()

query="""
insert into book(title,author,pages) values(%s,%s,%s)
"""

values=('throne of glass','sarah j maas',500)
cursor.execute(query,values)
connection.commit()

print("record has been inserted")
