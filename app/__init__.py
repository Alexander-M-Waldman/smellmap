from flask import Flask
# from flask_flash import Flash
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    print(f"Created app with name: {app.name}")
    print(f"Registered blueprints: {app.blueprints}")

    # Initialize the database with the app instance
    db.init_app(app)
    login_manager.init_app(app)

    # Register your Blueprints here
    from app.main import main_bp
    app.register_blueprint(main_bp)
    # from app.main.map_bp import bp as map_bp
    # app.register_blueprint(map_bp)
    
    # Setup flask_login 
    login_manager.init_app(app)
    login_manager.login_view = "main.login"  # Set the login view to redirect users to the login page

    return app


@login_manager.user_loader
def load_user(user_id):
    from .models import User
    return User.query.get(int(user_id))