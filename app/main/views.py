from flask import render_template,request,redirect,url_for, abort, flash

from app.auth.views import login
from . import main
from ..models import User, Pitch,Comment
from .forms import UpdateProfile,CommentForm, PitchesForm
from .. import db,photos
# we want to access the login functionality for some features eg voting and making a pitch
from flask_login import login_required,current_user

# def make_pitches(pitches):

#     new_pitches = []
#     for pitch in pitches:
#         user = User.query.filter_by(id=pitch.user_id).first()
#         category = category.query.filter_by(id=pitch.category_id).first()
#         comments = Comment.query.filter_by(pitch_id=pitch.id).all()
#         new_pitches.append({
#         'id': pitch.id,
#         'title': pitch.title,
#         'content': pitch.content,
#         'category': category,
#         'user': user,
#         'upvotes': pitch.upvotes,
#         'downvotes': pitch.downvotes,
#         })
#     print(new_pitches)    
#     return new_pitches
    



# Views
@main.route('/')
def index():
    
    all_pitches = Pitch.query.all()
    interviews = Pitch.query.filter_by(category="Interview-Pitch").order_by(Pitch.Additiontime.desc()).all()
    products = Pitch.query.filter_by(category="Product-Pitch").order_by(Pitch.Additiontime.desc()).all()
    promotions = Pitch.query.filter_by(category="Promotion-Pitch").order_by(Pitch.Additiontime.desc()).all()
    business = Pitch.query.filter_by(category="Business-Pitch").order_by(Pitch.Additiontime.desc()).all()
    pickUp = Pitch.query.filter_by(category="'Pick-up").order_by(Pitch.Additiontime.desc()).all()
    sales = Pitch.query.filter_by(category="'Pick-up").order_by(Pitch.Additiontime.desc()).all()
    
    
    title = "pitch & pitch"
    
    return render_template('index.html', title=title, all_pitches = all_pitches, interviews=interviews, products=products, promotions=promotions, business=business, pickUp = pickUp, sales=sales)


@main.route('/create_new', methods =['POST','GET'])
@login_required
def new_pitch():
    form = PitchesForm()
    if form.validate_on_submit():
        name = form.name.data
        pitchcontent = form.content.data
        category = form.category.data
        user_id = current_user
        new_pitch_object = Pitch( name = name, pitchcontent=pitchcontent,user_id=current_user._get_current_object().id,category=category)
        new_pitch_object.save_pitch()
        return redirect(url_for('main.index'))
        
    return render_template('newpitch.html', form = form)

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


#User comments
@main.route('/comment/<int:pitch_id>', methods = ['POST','GET'])
@login_required
def comment(pitch_id):
    form = CommentForm()
    pitch = Pitch.query.get(pitch_id)
    usercomments_list = Comment.get_comments(pitch_id)
    if form.validate_on_submit():
        comment_Message = form.comment_content.data 
        pitch_id = pitch_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment_Message = comment_Message, user_id = user_id,pitch_id = pitch_id)
        new_comment.save_comments()
        return redirect(url_for('.comment', pitch_id = pitch_id))
    return render_template('comments.html', form =form, pitch = pitch,usercomments_lists=usercomments_list)


@main.route('/create_new', methods =['POST','GET'])
@login_required
def downvote_pitch(pitch_id):

  pitch = Pitch.query.filter_by(id=pitch_id).first()
  if pitch:
    pitch.downvotes -= 1
    db.session.commit()
    flash('Vote added ----', 'success')
    return redirect(request.referrer)
  else:
    flash('No certain pitch', 'warning')
    return redirect(url_for('main.index'))

@main.route('/create_new', methods =['POST','GET'])
@login_required  
def upvote_pitch(pitch_id):
  pitch = Pitch.query.filter_by(id=pitch_id).first()
  if pitch:
    pitch.upvotes += 1
    db.session.commit()
    flash('Vote added --|===--', 'success')
    return redirect(request.referrer)
  else:
    flash('No certain pitch', 'warning')
    return redirect(url_for('main.index'))


