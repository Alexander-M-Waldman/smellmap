from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, TextAreaField, SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, NumberRange

class SmellForm(FlaskForm):
    latitude = FloatField('Latitude', validators=[DataRequired()])
    longitude = FloatField('Longitude', validators=[DataRequired()])
    smell_type = SelectField('Smell Type', choices=[], validators=[DataRequired()])
    intensity = IntegerField('Intensity', validators=[DataRequired(), NumberRange(min=0, max=10)])
    description = TextAreaField('Description', validators=[Optional(), Length(max=200)])
    submit = SubmitField('Submit Smell')

    def __init__(self, smell_types, *args, **kwargs):
        super(SmellForm, self).__init__(*args, **kwargs)
        self.smell_type.choices = [(smell_type.id, smell_type.name) for smell_type in smell_types]
