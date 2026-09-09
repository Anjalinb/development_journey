from mysql import connector

connection=connector.connect(
    user="root",
    password="root",
    host="localhost",
    database='song_db'
)

cursor=connection.cursor()
query="""
select * from song where id=%s;
"""
values=(2,)

cursor.execute(query,values)
records=cursor.fetchone()
print(records)