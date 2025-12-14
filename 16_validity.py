# 16 Python program to check the validity of username and password input by users

user={
    "ram":"ram123",
    "shyam":"shyam123"}

for attempt in range(1,4):
    username= input("Enter username: ")
    password= input("Enter password: ")

    if username in user and user[username]==password:
        print("login succesfully ")
        break

    else :
        print("Invalid username or passowrd")
        print("Attempt left:", 3-attempt)

if attempt==3:
    print("Account Locked. Too mamy attempt")
