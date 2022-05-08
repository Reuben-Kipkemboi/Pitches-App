from ast import Index
import datetime
import email
from enum import unique

from flask_login import UserMixin
from . import db, login_manager
#securing user passwords
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#Users table

class User( UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True) 
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True, index = True)
    avatar = db.Column(db.String())
    password_secure = db.Column(db.String(255))
    
    @property  #used to create a write only class property password
    def password(self):
        raise AttributeError('You are not allowed to read passcode')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)
    
    
    def __repr__(self):
        return f'User {self.username}'
      
    
#Pitch table

class Pitch(db.Model):
    __tablename__ = 'pitchTypes'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255),nullable = False)
    pitchcontent = db.Column(db.Text(), nullable = False)
    Additiontime = db.Column(db.DateTime, default = datetime.utcnow)
    category = db.Column(db.String(255), index = True,nullable = False)
    
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
  
    def __repr__(self):
        return f'Pitch {self.post}'
    
    
#User votes tables
#Upvote table

class Upvotes(db.Model):
    __tablename__ = 'user_upvotes'

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
