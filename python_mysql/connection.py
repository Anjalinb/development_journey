from mysql import connector

connection=connector.connect(
    user='root',
    password='root',
    host='localhost'
)

print(connection)