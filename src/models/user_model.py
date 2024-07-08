#se crea la clase User para manejar de forma mas eficiente la informacion
class User():
    
    def __init__(self, id=0, username = 0, password_hash = 0, email = 0) -> None:
        self.id = id
        self.username = username
        self.password_hash = password_hash
        self.email = email  
        