from flask import Flask 
from .config import Config
from .db import init_db

def create_app():

    app = Flask(__name__, static_folder='static', template_folder='templates')

    from .routes.home import home_bp
    from .routes.user import user_bp
    from .routes.api_integration import api_bp
    from .routes.ml_serving import ml_bp
    from .routes.llm_integration import llm_bp

    app.register_blueprint(home_bp)

    app.register_blueprint(user_bp, url_prefix='/user')

    app.register_blueprint(api_bp, url_prefix='/api')

    app.register_blueprint(ml_bp, url_prefix ='/ml')

    app.register_blueprint(llm_bp, url_prefix ='/llm')

    return app




