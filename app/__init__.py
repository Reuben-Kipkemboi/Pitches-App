from flask import Flask
from config import config_options
# making use of SQL ALchemy
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() # an instance

def create_app(config_name):
    
    app = Flask(__name__)
    
    
    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    
     # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    #Initializing the extensions from flask
    db.init_app(app)

    return app