from flask import Blueprint, render_template

signup_bp = Blueprint('signup', __name__)

@signup_bp.route('/', methods=['GET','POST'])
def SignUp_page():
    return render_template('signup.html',title = 'SignUp Page')