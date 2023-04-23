from datetime import datetime
from app import db

# db = SQLAlchemy()

class Smell(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    smell_type = db.Column(db.String(100), nullable=False)
    intensity = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    submitter_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    smell_type_id = db.Column(db.Integer, db.ForeignKey('smell_type.id'))
    smell_source_id = db.Column(db.Integer, db.ForeignKey('smell_source.id'))


    def __repr__(self):
        return f'<Smell {self.id}: {self.smell_type} ({self.intensity}) at ({self.latitude}, {self.longitude})>'
    

class SmellType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(200))
    smells = db.relationship('Smell', backref='smell_type_obj', lazy='dynamic')

    def __repr__(self):
        return f'<SmellType {self.name}>'


class SmellSource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(200))
    smells = db.relationship('Smell', backref='smell_source', lazy='dynamic')

    def __repr__(self):
        return f'<SmellSource {self.name}>'
    

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    smells = db.relationship('Smell', backref='submitter', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.username}>'

def init_app(app):
    db.init_app(app)

