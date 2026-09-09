employee={"id":100,"name":"Anjali","dept":'hr'}
key=input("Enter key:")
try:
    print(employee[key])
except Exception as e:
    print(e)
finally:
    print("db commit")


