from app import db
from app.models import Smell, SmellType, SmellSource, User
from app import create_app, db

app = create_app()
app.app_context().push()
db.create_all()
