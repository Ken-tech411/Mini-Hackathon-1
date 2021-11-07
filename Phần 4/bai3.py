import re
print("== Registration ==")
username_input = input("Username: ")

password_input = input("Password: ")
n = True
while n:
    if len(password_input) < 8:
        print("Password must be at least 8 characters long")
        password_input = input("Password: ")
    elif re.search('[a-z]', password_input) is None:
        print("Make sure your password has a number in it")
        password_input = input("Password: ")
    else:
        n = False
        break
if n == False:
    repeat_password = input("Repeat Password: ")
    while repeat_password != password_input:
        print("Password does not match. Please input again.")
        repeat_password = input("Repeat Password: ")



regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

email_input = input("Email: ")
x = True
while x:
    if re.search(regex, email_input) is None:
        print("Email is not valid")
        email_input = input("Email: ")
    else:
        x = False
        break
if x == False:
    print("Registered successfully")