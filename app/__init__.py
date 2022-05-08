from flask import Flask
from config import config_options
# making use of SQL ALchemy
from flask_sqlalchemy import SQLAlchemy

#**********Handling user login************************
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.session_protection = 'strong' #Enhances security levels by monitoring the changes in a user's request header and log the user out.
login_manager.login_view = 'auth.login'
#********User login ends here***********************

db = SQLAlchemy() # an instance

def create_app(config_name):
    
    app = Flask(__name__)
    
    
    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    
     # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    #Registering the authentication blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/user-authentication')
    
    #Initializing the extensions from flask
    db.init_app(app)
    login_manager.init_app(app)

    return app