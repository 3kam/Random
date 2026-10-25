def is_valid_username(username):
    if len(username) == 0 or len(username) > 8:
        return False

    if not username.isalpha():
        return False

    return True

user_input = input("Enter your username: ")

if is_valid_username(user_input):
    print("Username is Valid!")
else:
    print("Error: Must be no more than 8 Characters. Only uppercase and lowercase lettrs are accepted. < is not allowed, in preventaion of injecting code through the username")