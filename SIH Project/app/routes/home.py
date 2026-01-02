from flask import Flask, render_template, redirect, url_for, Blueprint

home_bp = Blueprint('Home',__name__)

@home_bp.route('/')
def home():
    return render_template('home.html')