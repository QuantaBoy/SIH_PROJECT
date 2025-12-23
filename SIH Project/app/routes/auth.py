from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from ..db import db
from ..models import User

auth_bp = Blueprint('auth',__name__)

@auth_bp.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password,password):
            return "Login Successful"
        return "invalid Credentials"
    return render_template("login.html")
@auth_bp.route('/signup',methods = ['GET','POST'])
def signup():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            return "Password do not match"
        hasp_pass = generate_password_hash(password)

        user = User(username = username,email=email,password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    
    return render_template('signup.html')