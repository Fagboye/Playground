import getpass

# create a data structure to hold the usernames and passwords 
login_info = {
    "Ola": "4506",
    "Oluwatobiloba": "2709"
    
}

# create input actions for username and password
username = input("what is your username? ")
password = getpass.getpass("what is your password? ")

# check if username is present in the database, and if the password matches the username, if not request for the password again 
for i,y in login_info.items():
    if i == username:
        no_tries = 0
        while password != y and no_tries != 2:
            print("password is wrong")
            password = getpass.getpass("Input password again? ")
            no_tries += 1
        if password == y:
            print("Login Successful")
        else:
            
            print("No of tries exceeded, login unsucessful")
        break
# I am adding this for fun
# adding sometthing for the branch 
