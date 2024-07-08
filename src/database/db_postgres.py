#librerias
from psycopg2 import connect
import jwt
from os import environ

#modulos
from src.models.user_model import User

#dvariables de entorno

key = environ.get("key")

user=environ.get("user")
password=environ.get("password")
host=environ.get("host")
port=environ.get("port")
database=environ.get("database")

#permite conectar a la db
def connect_to_db() -> None:
    conn = connect(
        user=user,
        password=password,
        host=host,
        port=port,
        database=database
    )

    return conn

#permite agregar un usuario
def add_user(self) -> None:
    username = self.username
    password_decoded = self.password_hash
    email = self.email
    password_encoded = jwt.encode({"password": password_decoded}, key, algorithm="HS256")
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, email, password_hash) VALUES (%s,%s,%s)", (username,email,password_encoded,))
    conn.commit()
    conn.close()

#permite chequear si el usuario ya existe
def check_user(username,email):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT username from users where username = %s union SELECT email from users where email = %s", (username,email))
    user = cursor.fetchall()
    conn.commit()
    conn.close()
    return user


#permite actualizar los datos de un usuario
    
def update_user(current_user, new_user) -> None:
    id = current_user.id
    new_username = new_user.username
    new_email = new_user.email
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute(
    'update users set username = %s, email = %s where id = %s',
        (new_username, new_email,id)
        )
    connection.commit()
    connection.close()

#permite obtener los datos de un usuario en especifico
def get_user_data(username,password_decoded):
    conn = connect_to_db()
    cursor = conn.cursor()
    password_encoded = jwt.encode({"password": password_decoded}, key, algorithm="HS256")
    cursor.execute("SELECT id,username,email from users where username = %s and password_hash = %s", (username,password_encoded))
    data = cursor.fetchall()
    conn.commit()
    conn.close()
    return data

def delete_user(username,password_decoded):
    conn = connect_to_db()
    cursor = conn.cursor()
    password_encoded = jwt.encode({"password": password_decoded}, key, algorithm="HS256")
    cursor.execute("DELETE from users where username = %s and password_hash = %s", (username,password_encoded))
    conn.commit()
    conn.close()
