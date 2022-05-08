from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from ..models import User
from wtforms import StringField, PasswordField, BooleanField, SubmitField

#user register form
class RegistrationForm(FlaskForm):
    email = StringField('Provide a valid Email Address',
                        validators=[DataRequired(), Email()])
    username = StringField('Provide your username',
                           validators=[DataRequired()])
    password = PasswordField('User Password', validators=[DataRequired(), EqualTo(
        'password_confirm', message='Your two Passwords must match')])
    password_confirm = PasswordField(
        'Confirm Your Password', validators=[DataRequired()])
    submit = SubmitField('click To Sign Up')
    
#login form  
class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators =[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log In')
    
    
