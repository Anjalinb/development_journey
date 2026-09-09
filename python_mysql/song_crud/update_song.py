from mysql import connector

connection=connector.connect(
    user="root",
    password="root",
    host='localhost',
    database='song_db'
)

cursor=connection.cursor()

query="""
update song set track_number=%s where id=%s
"""

values=(3,3)
cursor.execute(query,values)

connection.commit()
print("record has been updated")