from flask import Blueprint, render_template
login_bp = Blueprint('login',__name__)

@login_bp.route('/',methods = ['GET','POST'])
def login_page():
    return render_template('login.html', title = 'Login Page')