from flask import render_template, redirect, url_for, request, flash
from sqlalchemy.orm import joinedload
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


    return render_template('submit_smell.html', form=form)



@bp.route('/view_map')
def view_map():
    smells = Smell.query.all()
    return render_template('view_map.html', smells=smells)


@bp.route('/admin')
def admin():
    # You can fetch the data you want to display from a database or any other source
    # For this example, let's use some dummy data
    # smells = Smell.query.all()
    smells = Smell.query.options(joinedload(Smell.smell_type)).all()

    return render_template('admin.html', smells=smells)