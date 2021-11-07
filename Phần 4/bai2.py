print("== Registration ==")
username_input = input("Username: ")

password_input = input("Password: ")
repeat_password = input("Repeat Password: ")
while repeat_password != password_input:
    print("Password does not match. Please input again.")
    repeat_password = input("Repeat Password: ")

email_input = input("Email: ")


print("Registered successfully")