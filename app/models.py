from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from datetime import datetime
from app import db



# db = SQLAlchemy()

class Smell(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    intensity = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    submitter_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    smell_type_id = db.Column(db.Integer, db.ForeignKey('smell_type.id'))
    smell_source_id = db.Column(db.Integer, db.ForeignKey('smell_source.id'))

    # Add a relationship property to link the Smell and SmellType models
    smell_type = relationship("SmellType", backref="smells")



    def __repr__(self):
        return f'<Smell {self.id}: {self.smell_type} ({self.intensity}) at ({self.latitude}, {self.longitude})>'
    

class SmellType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(200))
    # smells = db.relationship('Smell', backref='smell_type_obj', lazy='dynamic')
    color = db.Column(db.String(7))

    # Add a relationship property to link the SmellType and Smell models
    # smells = relationship("Smell", back_populates="smell_type")

    def __repr__(self):
        return f'<SmellType {self.name}>'


class SmellSource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(200))
    smells = db.relationship('Smell', backref='smell_source', lazy='dynamic')

    def __repr__(self):
        return f'<SmellSource {self.name}>'
    

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    smells = db.relationship('Smell', backref='submitter', lazy='dynamic')
    is_validator = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<User {self.username}>'
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


def init_app(app):
    db.init_app(app)

