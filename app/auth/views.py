from flask import render_template,redirect,url_for, flash, request
#Flash function helps in displaying error message to the user.....
from flask_login import login_user, logout_user, login_required
from ..models import User
from . import auth
from .forms import RegistrationForm,LoginForm
from .. import db
from ..email import mail_message


#Register view
@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        
        mail_message("Welcome to Pitch & Pitch, Pitch to Impress","email/welcome_user",user.email,user=user)
        return redirect(url_for('auth.login'))
    
    
    title="Pitch & Pitch New User Account"
    return render_template('auth/register.html',registration_form = form, title = title)


#User login view
@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Hello, Your username or Password is invalid')

    title = "Pitch & pitch login"
    return render_template('auth/login.html',login_form = login_form,title=title)

#LOgout view
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
#This will logout the user pitch&Pitch  application, then redirects the user to the index page.