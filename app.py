#librerias

from flask import Flask
from flask_cors import CORS

#modulos

from src.routes import api_routes

app = Flask(__name__)
CORS(app)


#registro de blueprints

app.register_blueprint(api_routes.main)


if __name__ == "__main__":
    app.run(debug=True)