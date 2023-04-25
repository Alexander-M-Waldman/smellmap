from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, TextAreaField, SelectField, IntegerField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Optional, NumberRange, Email, EqualTo

class SmellForm(FlaskForm):
    latitude = FloatField('Latitude', validators=[DataRequired()])
    longitude = FloatField('Longitude', validators=[DataRequired()])
    smell_type = SelectField('Smell Type', choices=[], validators=[DataRequired()])
    intensity = IntegerField('Intensity', validators=[DataRequired(), NumberRange(min=0, max=10)])
    description = TextAreaField('Description', validators=[Optional(), Length(max=200)])
    submit = SubmitField('Submit Smell')

    def __init__(self, smell_types, *args, **kwargs):
        super(SmellForm, self).__init__(*args, **kwargs)
        self.smell_type.choices = [(str(smell_type.id), smell_type.name) for smell_type in smell_types]
        # self.smell_type.choices = [(smell_type.id, smell_type.name) for smell_type in smell_types]


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=64)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')