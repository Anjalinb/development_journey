db_username="anjali"
db_password="3214"
username=input("Enter username:")
if db_username==username:
    password=input("Enter password:")
    if db_password==password:
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Invalid username")