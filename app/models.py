from datetime import datetime
import email
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
    pitch_types = db.relationship('Pitch', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref='user', lazy='dynamic')
    upvote = db.relationship('Upvotes',backref='user',lazy='dynamic')
    downvote = db.relationship('Downvotes',backref='user',lazy='dynamic')
    
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
    __tablename__ = 'pitch_types'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255),nullable = False)
    pitchcontent = db.Column(db.Text(), nullable = False)
    Additiontime = db.Column(db.DateTime, default = datetime.utcnow)
    category = db.Column(db.String(255), index = True,nullable = False)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comment = db.relationship('Comment',backref='pitch_types',lazy='dynamic')
    upvote = db.relationship('Upvotes',backref='pitch_types',lazy='dynamic')
    downvote = db.relationship('Downvotes',backref='pitch_types',lazy='dynamic')
    
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_user_pitches(cls,pitch_type_category):
        user_pitches = Pitch.query.filter_by(category=pitch_type_category).all()
        return user_pitches
  
    def __repr__(self):
        return f'Pitch {self.pitchcontent}'
    
    
#User votes tables
#Upvote table

class Upvotes(db.Model):
    __tablename__ = 'user_upvotes'

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitch_types.id'))
      
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_upvotes(cls,id):
        user_upvote = Upvotes.query.filter_by(pitch_types_id=id).all()
        return user_upvote
  
#Downvotes table

class Downvotes(db.Model):
    __tablename__ = 'user_downvotes'

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitch_types.id'))
    # kigibu@mailinator.com
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_downvotes(cls,id):
        user_downvote = Downvotes.query.filter_by(pitch_types_id=id).all()
        return user_downvote
    
    
#User comments table

class Comment(db.Model):
    __tablename__ = 'user_comments'
    id = db.Column(db.Integer, primary_key=True)
    comment_Message = db.Column(db.Text(),nullable = False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable = False)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitch_types.id'),nullable = False)

    def save_comments(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,pitch_id):
        user_comments = Comment.query.filter_by(pitch_types_id=pitch_id).all()

        return user_comments
    


