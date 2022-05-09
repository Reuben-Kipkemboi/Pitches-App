from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField, SubmitField
from wtforms.validators import DataRequired

#User update profile
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Briefly describe yourself.',validators = [DataRequired()])
    submit = SubmitField('Submit')


class PitchesForm(FlaskForm):
    name = StringField('Author Name ', validators=[DataRequired()])
    content = TextAreaField('Enter Your one minute pitch', validators=[DataRequired()])
    
    category = SelectField('Category', choices=[('Product-Pitch','Product Pitch'),('Pick-up' ,'Pick Up Lines'),('Sales-Pitch','Sales Pitch'),('Interview-Pitch','Interview Pitch'),('Promotion-Pitch','Promotion Pitch'),('Business-Pitch','Business Pitch')], validators=[DataRequired()])
    submit = SubmitField('Pitch with Impress')

class CommentForm(FlaskForm):
    comment_content = TextAreaField('Provide feedback/Comments', validators=[DataRequired()])
    submit = SubmitField('Add Comment')