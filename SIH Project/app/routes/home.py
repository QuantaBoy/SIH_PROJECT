from flask import Blueprint, render_template, jsonify

home_bp = Blueprint('home',__name__,template_folder=r'app\Templates')

@home_bp.route('/',methods = ['GET'])
def home():
    return render_template("home.html",title="Home Page")

