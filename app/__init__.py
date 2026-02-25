from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    
    from .routes.auth import auth_bp
    from .routes.scores import scores_bp
    from .routes.users import users_bp 

    app.register_blueprint(auth_bp)
    app.register_blueprint(scores_bp)
    app.register_blueprint(users_bp) 

    return app