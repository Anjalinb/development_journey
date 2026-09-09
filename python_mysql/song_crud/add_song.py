from mysql import connector

connection=connector.connect(
    user='root',
    password='root',
    host='localhost',
    database='song_db'
)

cursor=connection.cursor()

query="""
insert into song(title,track_number,movie,singers) values(%s,%s,%s,%s);
"""
values=("thee minnal",2,"minnal murali","vineeth")
cursor.execute(query,values)
connection.commit()
connection.close()
print("record inserted")