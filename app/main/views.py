from flask import render_template,url_for
from . import main
# we want to access the login functionality for some features eg voting and making a pitch
from flask_login import login_required


# Views
@main.route('/')
def index():
    
    
    title = "pitch & pitch"
    
    return render_template('index.html',title=title)

