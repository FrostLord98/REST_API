#permite verificar que dato es el que existe en la db
def info_on_check_user(data):
    if len(data) == 2:
        return "username and email already registered"
    for i in data:
        if i[0].find("@") != -1:
            return "email already registered"
        else:
            return "username already registered"
        


    