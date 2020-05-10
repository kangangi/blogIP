import os 
class Config:
    '''
    General Configuration parent class
    '''
    SECRET_KEY = "Skylar"
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    QUOTES_API = "http://quotes.stormconsultancy.co.uk/random.json"


class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    PDevelopment  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://diana:12345@localhost/blog'
    DEBUG = True 

config_options ={
    'production': ProdConfig,
    'development': DevConfig
}
