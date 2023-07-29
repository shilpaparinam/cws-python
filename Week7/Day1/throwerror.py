try:
    name = input("enter your name")
    pwd = input("enter the password")
    if name == "admin" and pwd == "admin":
        print("successfully logged in")
    else:
        raise Exception("wrong pwd")
#except Exception as e:
    #print(e)
