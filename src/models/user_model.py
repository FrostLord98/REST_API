import pytz
from datetime import datetime #esto nos permite adjuntar la fecha y hora de creacion del usuario

#se crea la clase User para manejar de forma mas eficiente la informacion
class User():
    
    def __init__(self, id=0, username = 0, password_hash = 0, email = 0,created_at = lambda: datetime.now(pytz.timezone("America/Caracas"))) -> None:
        self.id = id
        self.username = username
        self.password_hash = password_hash
        self.email = email  
        self.created_at = created_at
        
