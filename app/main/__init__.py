from flask import Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy



main_bp = Blueprint('main', __name__)
# import routes
from app.main import routes

# bp = Blueprint('main', __name__)
# map_bp = Blueprint('map_bp', __name__)

# @map_bp.route('/map')
# def show_map():
#     return render_template('map.html')

# main_bp = Blueprint('main', __name__)

# @main_bp.route('/')
# def index():
#     return render_template('index.html')

# @main_bp.route('/login')
# def login():
#     return render_template('login.html')

# @main_bp.route('/register')
# def register():
#     return render_template('register.html')

# @main_bp.route('/logout')
# def logout():
#     return render_template('index.html')
