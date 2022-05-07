from flask import render_template,url_for
from . import main


# Views
@main.route('/')
def index():
    
    
    title = "pitch & pitch"
    
    return render_template('index.html',title=title)

