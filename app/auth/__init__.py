from flask import Blueprint #Geting the blueprint

auth = Blueprint('auth',__name__)

from . import views