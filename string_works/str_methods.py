password="hello8=@678"
if password.isalpha():
    print("Password is an alphabet")
elif password.isdigit():
    print('Password is digit')
elif password.isalnum():
    print("Password is alphanumeric")
else:
    print("Special character")
