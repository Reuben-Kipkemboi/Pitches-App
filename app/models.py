from . import db
#securing user passwords
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True) 
    username = db.Column(db.String(255))
    password_secure = db.Column(db.String(255))
    
    
    @property  #used to create a write only class property password
    def password(self):
        raise AttributeError('You are not allowed to read passcode')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    
    
    def __repr__(self):
        return f'User {self.username}'