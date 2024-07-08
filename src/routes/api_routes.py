#librerias
from flask import Blueprint,request,jsonify

#modulos
import src.database.db_postgres as db
from src.models.user_model import User
from src.services.check_user_service import info_on_check_user
from src.utils.auth_jwt import Security

main = Blueprint("main", __name__)

#ruta que permite agregar un usuario
@main.route("/register", methods=["POST"])
def add_user():
    username = request.form["username"]
    email = request.form["email"]
    password_hash = request.form["password"]
    try:
        assert username and email and password_hash is not None
    except:
        return "all fields are required",400
    data = db.check_user(username,email) #chequea si el usuario ya existe
    
    if len(data) == 0:
        user = User(username = username, password_hash = password_hash, email = email) #crea un objeto de la clase User y luego lo agrega a la db
        db.add_user(user)
        return jsonify({"payload":"success"})
    
    else:
        return info_on_check_user(data),401 #devuelve el error si el nombre o el correo o los dos existen e indica cual


#logea al usuario y genera un token
@main.route("/login", methods=["POST"])
def login():
    password_hash = request.form["password"]
    username = request.form["username"]
    data = db.get_user_data(username,password_hash)# trae la informacion de la db
    try:
        user = User(id=data[0][0],username=data[0][1], email=data[0][2],password_hash=password_hash) #crea un objeto de la clase User
        token = Security.create_token(user) #genera el token
        return token,200
    except:
        return "user not registered",401
        
    
#decodifica el token y trae los datos del usuario que lo genero
@main.route("/user", methods=["get"])
def get_user():
    has_access = Security.verify_token(request.headers)
    if has_access: #verifica si el token es valido
        has_access.pop("iat")#elimina la fecha de creacion
        has_access.pop("exp")#elimina la fecha de expiracion
        return jsonify({"user":has_access,
                        "payload":"success"})
    else:
        return jsonify({"response":"Unauthorized"}),401



 #actualiza los datos del usuario        
@main.route("/user" , methods=["put"])
def update_user():
    has_access = Security.verify_token(request.headers) #verifica el token
    if has_access:
        has_access.pop("iat") #elimina la fecha de creacion
        has_access.pop("exp") #elimina la fecha de expiracion
        username = request.form["username"] #obtiene los datos del formulario
        email = request.form["email"] #obtiene los datos del formulario
        #trae la informacion de la db
        #crea un objeto de la clase User
        current_user = User(id = has_access["id"], username = has_access["username"], email = has_access["email"])
        new_user = User(username = username, email = email, password_hash = has_access["password_hash"])
        data = db.check_user(username,email) #chequea si el usuario ya existe

        if len(data) == 1: #si len(data) == 1 es porque el email o el nombre existe

            # se verifica si el dato existente es del usuario mismo
            if data[0][0] == current_user.username or data[0][0] == current_user.email:
                db.update_user(current_user,new_user) #de ser el caso se actualiza el usuario para agregar el nuevo dato en la db 
                temporal = db.get_user_data(new_user.username,new_user.password_hash)
                new_user = User(id = temporal[0][0], username = temporal[0][1], email = temporal[0][2], password_hash = has_access["password_hash"])
                token = Security.create_token(new_user) #genera el token con los nuevos datos del usuario
                return jsonify({"data":token,"payload":"success"})
            else:
                return info_on_check_user(data),401
        
        
        elif len(data) == 0: #si len(data) == 0 es porque el email y el nombre no existen
            db.update_user(current_user,new_user) #se actualiza el usuario con ambos datos ya que no existen previamente
            token = Security.create_token(new_user) #genera el token con los nuevos datos del usuario

            return jsonify({"data":token,"payload":"success"})
        
        else:
            return info_on_check_user(data),401
    
    else:
        return jsonify({"response":"Unauthorized"}),401
        

#elimina el usuario autenticado    
@main.route("/user" , methods=["delete"])
def delete_user():
    has_access = Security.verify_token(request.headers) #verifica el token
    #usando los datos del token decodificado se verifica que el usuario exista en el sistema
    if has_access:
        has_access.pop("iat")
        has_access.pop("exp")
        username = has_access["username"]
        password = has_access["password_hash"]
        email = has_access["email"]
        data = db.check_user(username,email)
        #si no existe se devuelve un error 404
        if len(data) == 0:
            return "user does not exist",404
        #si existe se elimina satisfactoriamente
        db.delete_user(username,password)
        return jsonify({"payload":"success"})
    #si no se encuentra el token se devuelve un error 401
    else:
        return jsonify({"response":"Unauthorized"}),401
        

    