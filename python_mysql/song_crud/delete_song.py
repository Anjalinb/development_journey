from mysql import connector

connection=connector.connect(
    user="root",
    password="root",
    host='localhost',
    database='song_db'
)

cursor=connection.cursor()

query="""
delete from song where id=%s
"""

values=(3,)
cursor.execute(query,values)

connection.commit()
print("record has been deleted")