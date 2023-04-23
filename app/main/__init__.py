from flask import Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy


bp = Blueprint('main', __name__)

# import routes
import app.main.routes

map_bp = Blueprint('map_bp', __name__)

@map_bp.route('/map')
def show_map():
    return render_template('map.html')

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')