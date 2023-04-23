from flask import Flask
# from flask_flash import Flash
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    # flash = Flash(app)

    print(f"Created app with name: {app.name}")
    print(f"Registered blueprints: {app.blueprints}")

    # Initialize the database with the app instance
    from app.models import init_app
    init_app(app)

    # Register your Blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    from app.main.map_bp import bp as map_bp
    app.register_blueprint(map_bp)
    # ...

    return app

