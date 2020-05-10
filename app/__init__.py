from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet,configure_uploads,IMAGES



db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
photos = UploadSet('photos', IMAGES)


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

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #configure UploadSet
    configure_uploads(app,photos)
    return app 