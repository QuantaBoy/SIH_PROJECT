from flask import Flask
from .config import Config
from .db import db

def app_run():
    
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from .routes.auth import auth_bp
    app.register_blueprint(auth_bp,url_prefix = '/auth')

    from .routes.subscription import subscription_bp
    app.register_blueprint(subscription_bp,url_prefix = '/subscription')

    from .routes.home import home_bp
    app.register_blueprint(home_bp,url_prefix='/')

    from app.routes.leetcode_routes import leetcode_bp
    app.register_blueprint(leetcode_bp,url_prefix='/leetcode')

    from app.routes.profile_routes import profile_bp
    app.register_blueprint(profile_bp,url_prefix='/profile')

    with app.app_context():
        db.create_all()

    return app