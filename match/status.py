status=int(input("Enter the status code (2,3,4,5):"))
match status:
    case 2:
        print("Success")
    case 3:
        print("Redirect")
    case 4:
        print("Client Error")
    case 5:
        print("Server Error")
    case _:
        print("Invalid code")
  