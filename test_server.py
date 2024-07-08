import pytest
import json
import os
from app import app



os.environ['CONFIG_TYPE'] = 'config.TestingConfig'

#prueba para verificar la funcionalidad de la ruta de registro de un usuario
def test_add_user():
    with app.test_client() as client:
        #data que se envia al servidor
        email = "e@e.e"
        username = "echo"
        password = "abc123"
        data = {
            'email': email,
            'username': username,
            'password': password
        }
        endpoint = '/register'
        #se envia la peticion POST y se obtiene la respuesta
        response = client.post(endpoint, data=data)
        #se verifica que la respuesta sea 200
        assert response.status_code == 200
                                    

#prueba para verificar la funcionalidad de la ruta de login de un usuario    
def test_login_user():
    with app.test_client() as client:
        #data que se envia al servidor
        email = "e@e.e"
        username = "echo"
        password = "abc123"
        data = {
            'email': email,
            'username': username,
            'password': password
        }
        endpoint = '/login'
        #se envia la peticion POST y se obtiene la respuesta
        response = client.post(endpoint, data=data)
        data = response.data
        print(data)
        #se verifica que la respuesta sea 200 y que el token exista
        assert response.status_code == 200
        assert data

def test_get_user():
    with app.test_client() as client:
        endpoint = '/user'
        #el bearer token se registra de la prueba test_login usando pytest -s -v test_server.py::test_login_user y se copia de la consola a la variable token
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MjA0NzgxMjQsImV4cCI6MTcyMDQ4NDEyNCwidXNlcm5hbWUiOiJlY2hvIiwiZW1haWwiOiJlQGUuZSIsInBhc3N3b3JkX2hhc2giOiJhYmMxMjMiLCJpZCI6MjF9.vHAgeJ54rxeltHpKKJ_l4gKkcR3ltF4RCpqM91Slui0"
        headers = {'Authorization':'Bearer {}'.format(token)}
        #se envia la peticion GET y se obtiene la respuesta
        response = client.get(endpoint, headers=headers)
        data = json.loads(response.data)
        #se verifica que la respuesta sea 200
        assert response.status_code == 200
        assert data["payload"] == "success"

#prueba para verificar la funcionalidad de la ruta de borrar un usuario
def test_delete_user():
    with app.test_client() as client:
        endpoint = '/user'
        #el bearer token se registra de la prueba test_login usando pytest -s -v test_server.py::test_login_user y se copia de la consola a la variable token
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MjA0NzgxMjQsImV4cCI6MTcyMDQ4NDEyNCwidXNlcm5hbWUiOiJlY2hvIiwiZW1haWwiOiJlQGUuZSIsInBhc3N3b3JkX2hhc2giOiJhYmMxMjMiLCJpZCI6MjF9.vHAgeJ54rxeltHpKKJ_l4gKkcR3ltF4RCpqM91Slui0"
        headers = {'Authorization':'Bearer {}'.format(token)}
        #se envia la peticion delete y se obtiene la respuesta
        response = client.delete(endpoint, headers=headers)
        #se verifica que la respuesta sea 200
        assert response.status_code == 200
        assert response.data


def test_update_user():
    with app.test_client() as client:
        #data que se envia al servidor
        email = "e@e.e"
        username = "echo"
        password = "abc123"
        data = {
            'email': email,
            'username': username,
            'password': password
        }

        #el bearer token se registra de la prueba test_login usando pytest -s -v test_server.py::test_login_user y se copia de la consola a la variable token
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MjA0NzgxMjQsImV4cCI6MTcyMDQ4NDEyNCwidXNlcm5hbWUiOiJlY2hvIiwiZW1haWwiOiJlQGUuZSIsInBhc3N3b3JkX2hhc2giOiJhYmMxMjMiLCJpZCI6MjF9.vHAgeJ54rxeltHpKKJ_l4gKkcR3ltF4RCpqM91Slui0"
        headers = {'Authorization':'Bearer {}'.format(token)}
        endpoint = '/user'
        #se envia la peticion GET y se obtiene la respuesta
        response = client.put(endpoint, headers=headers,data=data)
        #se verifica que la respuesta sea 200
        assert response.status_code == 200
        assert response.data