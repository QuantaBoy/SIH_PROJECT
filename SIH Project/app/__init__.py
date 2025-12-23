from flask import Flask
from .config import Config
from .db import db

def app_run():
    
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from .routes.auth import auth_bp

    app.register_blueprint(auth_bp,url_prefix = '/auth')

    with app.app_context():
        db.create_all()

    return app