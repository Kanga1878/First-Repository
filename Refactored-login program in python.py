users = {"user1": "password1", "user2": "password2"}

def valid_user(username):
    if username in users:
        return True
         

def passcheck(username,password):
    if users[username] == password:
        return True

            
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if valid_user(username) != True:
            print("Username not found.")
            return
    if passcheck(username,password) != True:
            print("Incorrect Password.")
    else:
        print("Login Successful")
    
login()
#Olly
