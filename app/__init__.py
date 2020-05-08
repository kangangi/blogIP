from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    #Initialize app
    app = Flask(__name__)

    #Creating app configuration
    app.config.from_object(config_options[config_name])

    #Initializing flask extentions
    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)

    #Register blueprints
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app 