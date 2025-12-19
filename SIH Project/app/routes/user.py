from flask import Blueprint, render_template

user_bp = Blueprint("user", __name__, template_folder = r'app\Templates')

@user_bp.route('/',methods = ['GET'])
def user_home():
    return render_template('user.html', title = "User DashBoard")

@user_bp.route('/profile',methods = ['GET'])
def profile_page():
    return render_template('profile.html')