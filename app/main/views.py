from flask import render_template,request,redirect,url_for, abort
from . import main
from ..models import User
from .forms import UpdateProfile
from .. import db,photos
# we want to access the login functionality for some features eg voting and making a pitch
from flask_login import UserMixin, login_required,current_user


# Views
@main.route('/')
def index():
    
    
    title = "pitch & pitch"
    
    return render_template('index.html', title=title)

# The profile where users will view their previous pitches
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404) #stops a requests

    return render_template("userProfile/profile.html", user = user)


#Update user profile
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('userProfile/update.html',form =form)
#updating user profile image
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.avatar = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

