"""✅ 3. Login System with Password and OTP

Task:
Ask for password.

If password is correct:

Ask for OTP

If OTP is correct → "Login successful"

Else → "Incorrect OTP"


Else → "Incorrect password" """

db_password="1234"
db_otp=9090
password=input("Enter password:")
if db_password==password:
    otp=int(input("Enter otp:"))
    if db_otp==otp:
        print("Login successful")
    else:
        print("Incorrect otp!")
else:
    print("Incorrect password")