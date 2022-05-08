from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired

#User update profile
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Briefly describe yourself.',validators = [DataRequired()])
    submit = SubmitField('Submit')
