from flask import render_template, redirect, url_for, request, flash
from app.main import bp
from app.models import Smell, SmellType, SmellSource, User
from app.forms import SmellForm
from app import db


@bp.route('/', methods=['GET', 'POST'])
def index():
    # form = SmellForm()  # Create an instance of the form class
    smells = Smell.query.all()  # Query all smells from the database
    smell_types = SmellType.query.all()
    form = SmellForm(smell_types=smell_types)
    print("rendering index.html...")
    # print(render_template('index.html', form=form, smells=smells))  # Pass the form instance and smells to the template
    return render_template('index.html', form=form, smells=smells)


@bp.route('/submit_smell', methods=['GET', 'POST'])
def submit_smell():
    print("submit_smell function entered")
    smell_types = SmellType.query.all()
    form = SmellForm(smell_types) 
    # form = SmellForm()
    form.smell_type.choices = [(str(smell_type.id), smell_type.name) for smell_type in SmellType.query.order_by(SmellType.name).all()]

    if form.validate_on_submit():
        smell = Smell(
            latitude=form.latitude.data,
            longitude=form.longitude.data,
            smell_type=form.smell_type.data,
            intensity=form.intensity.data,
            description=form.description.data
        )
        db.session.add(smell)
        print("before commit")
        try:
            db.session.commit()
            print('after commit')
        except Exception as e:
            db.session.rollback()
            print(f'Error committing transaction: {e}')
            flash('Failed to submit smell!')
            return redirect(url_for('main.submit_smell'))
        flash('Smell submitted successfully!')
        return redirect(url_for('main.index'))
        # return redirect(url_for('map_bp.map'))

    # print(f"form: {form}")
    # print(f"errors: {form.errors}")
    # print(f"csrf_token: {form.csrf_token}")
    # print(f"latitude: {form.latitude}")
    # print(f"longitude: {form.longitude}")
    # print(f"smell_type: {form.smell_type}")
    # print(f"intensity: {form.intensity}")
    # print(f"description: {form.description}")
    
    else:
        flash('Please fill in all required fields')
        return redirect(url_for('main.index'))


    return render_template('submit_smell.html', form=form)



@bp.route('/view_map')
def view_map():
    smells = Smell.query.all()
    return render_template('view_map.html', smells=smells)