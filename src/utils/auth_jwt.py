import pytz
import jwt
import datetime
from os import environ

#se crea la clase Security para manejar todo lo relacionado con jwt

class Security():
    key = environ.get("key")
    tz = pytz.timezone("America/Caracas")

    #permite crear el token usando los datos del usuario
    @classmethod 
    def create_token(cls,user):
        payload={
            "iat":datetime.datetime.now(tz=cls.tz),
            "exp":datetime.datetime.now(tz=cls.tz) + datetime.timedelta(minutes = 100),
            "username":user.username,
            "email":user.email,
            "password_hash":user.password_hash,
            "id":user.id
        }
        return jwt.encode(payload,cls.key,algorithm="HS256") #regresa el token creado
    
    #verifica que el token sea valido
    @classmethod
    def verify_token(cls,headers):
        if "Authorization" in headers.keys():
            authorization = headers["Authorization"]

            encoded_token = authorization.split(" ")[1]

            try:
                #regresa el token decodificado en los elementos que los crearon, "iat","username" etc, o False si el token no es valido
                return  jwt.decode(encoded_token,cls.key,algorithms="HS256") 
              
            except(jwt.ExpiredSignatureError,jwt.InvalidSignatureError):
                return False
        return False
    

