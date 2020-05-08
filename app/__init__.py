from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_name):
    #Initialize app
    app = Flask(__name__)

    #Creating app configuration
    app.config.from_object(config_options[config_name])

    #Initializing flask extentions
    db.init_app(app)

    return app 