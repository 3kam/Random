username = input("Enter your username: ")
password = input("Enter your password: ")

expected_password = username[:3] + "123"

if password == expected_password:
    print(f"Welcome {username}")
else:
    ("Error")