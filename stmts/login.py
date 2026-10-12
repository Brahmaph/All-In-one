username = input("Enter user name: ")
password = input("Enter password: ")

if username == "admin":
    if password == "1234":
        print("Login Successfull")
    else:
        print("Invalid password")
else:
        print("Invalid username")