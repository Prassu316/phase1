def login():
    while(True):
        username=input("enter username")
        password=input("enter password")
        if (username==password):
            print("login successful")
            break
        else:
            print("enter correct username or password")
login()

