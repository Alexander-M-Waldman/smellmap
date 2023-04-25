from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from sqlalchemy.orm import joinedload
from config import Config
from app.main import main_bp
from app.models import Smell, SmellType, SmellSource, User
from app.forms import SmellForm, RegistrationForm, LoginForm
from app import db


@main_bp.route('/', methods=['GET', 'POST'])
def index():
    geocoder_url = Config.GEOCODER_URL    
    smells = Smell.query.all()  # Query all smells from the database
    smell_types = SmellType.query.all()
    form = SmellForm(smell_types=smell_types)
    form.smell_type.choices = [(str(smell_type.id), smell_type.name) for smell_type in SmellType.query.order_by(SmellType.name).all()]
    print("starting index route...")
    # print(render_template('index.html', form=form, smells=smells))  # Pass the form instance and smells to the template
    return render_template('index.html', form=form, smells=smells, geocoder_url=geocoder_url)
    # return render_template('index.html', smells=smells)



@main_bp.route('/submit_smell', methods=['GET', 'POST'])
def submit_smell():
    print("submit_smell function entered")
    smell_types = SmellType.query.all()
    form = SmellForm(smell_types) 
    print("form: ", form)
    form.smell_type.choices = [(str(smell_type.id), smell_type.name) for smell_type in SmellType.query.order_by(SmellType.name).all()]
    print(form.smell_type.choices)
    if form.validate_on_submit():
        print("smell type data: ", form.smell_type.data)
        smell_type = SmellType.query.filter_by(id=form.smell_type.data).first()
        print("smell_type query result: ", smell_type)
        for field in form._fields:
            v = form[field].data
            print(field, v, type(v))
        smell = Smell(
            latitude=form.latitude.data,
            longitude=form.longitude.data,
            smell_type_id=smell_type.id,
            intensity=form.intensity.data,
            description=form.description.data
        )

        db.session.add(smell)
        try:
            print("committing smell report...")
            db.session.commit()
            print("committed!")
        except Exception as e:
            db.session.rollback()
            print(f'Error committing transaction: {e}')
            flash('Failed to submit smell!', 'error')
            return redirect(url_for('main.submit_smell'))
        flash('Smell submitted successfully!', 'info')
        return redirect(url_for('main.index'))
        # return redirect(url_for('map_bp.map'))
    
    else:
        flash('Please fill in all required fields', 'error')
        return redirect(url_for('main.index'))
        # return

    print(form)
    return render_template('submit_smell.html', form=form)



@main_bp.route('/view_map')
def view_map():
    smells = Smell.query.all()
    # return render_template('view_map.html', smells=smells)
    geocoder_url = Config.GEOCODER_URL    
    return render_template(url_for('main.view_map'), smells=smells)


@main_bp.route('/admin')
def admin():
    # You can fetch the data you want to display from a database or any other source
    # For this example, let's use some dummy data
    # smells = Smell.query.all()
    smells = Smell.query.options(joinedload(Smell.smell_type)).all()

    return render_template('admin.html', smells=smells)


@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('main.login'))
    return render_template('register.html', title='Register', form=form)

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Add your authentication logic here
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
        else:
            flash('Invalid email or password')
    return render_template('login.html', title='Sign In', form=form)


@main_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))