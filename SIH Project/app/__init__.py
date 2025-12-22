from flask import Flask

def app_run():
    
    app = Flask(__name__, static_folder='static', template_folder='templates')

    from .routes.login import login_bp
    from .routes.signup import signup_bp

    app.register_blueprint(login_bp,url_prefix = '/login')
    app.register_blueprint(signup_bp, url_prefix='/signup')

    return app