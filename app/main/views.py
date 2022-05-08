from flask import render_template,url_for, abort
from . import main
from ..models import User
# we want to access the login functionality for some features eg voting and making a pitch
from flask_login import login_required


# Views
@main.route('/')
def index():
    
    
    title = "pitch & pitch"
    
    return render_template('index.html',title=title)

#The profile where users will view their previous pitches
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404) #stops a requests

    return render_template("userProfile/profile.html", user = user)

