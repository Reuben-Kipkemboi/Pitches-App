import os
class Config:
    '''
    General configuration parent class
    
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/dbpitches'
    # the destination for our uploaded images will be static folder
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    

    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = "postgresql://dagmdgfiqthkke:3ae2085f0190fc7df62f37c701ea08f158a70b9936421ec2130f6a1faa17e9bb@ec2-34-231-177-125.compute-1.amazonaws.com:5432/de9lr0qedhl3tc"
    
class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True   
config_options = {
'development':DevConfig,
'production':ProdConfig
}
