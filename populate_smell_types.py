from app import create_app, db
from app.models import SmellType

app = create_app()


# Define a list of smell types to be added to the database
smell_types = [
    {"name": "Sweet", "description": "Pleasant, sugary smells"},
    {"name": "Sour", "description": "Sharp, acidic smells"},
    {"name": "Salty", "description": "Sea-like or mineral smells"},
    {"name": "Bitter", "description": "Harsh, acrid smells"},
    {"name": "Earthy", "description": "Soil-like or damp smells"},
    {"name": "Fruity", "description": "Fresh, fruity smells"},
    {"name": "Floral", "description": "Sweet, flowery smells"},
    {"name": "Spicy", "description": "Strong, peppery smells"},
    {"name": "Woody", "description": "Resinous, bark-like smells"},
    {"name": "Chemical", "description": "Pungent, synthetic smells"},
    {"name": "Smoky", "description": "Burnt, acrid smells from smoke or fires"},
    {"name": "Industrial", "description": "Heavy, oily smells from factories or machinery"},
    {"name": "Sewage", "description": "Foul, unpleasant odors from sewage or waste"},
    {"name": "Exhaust", "description": "Pungent, acrid smells from vehicle exhaust"},
    {"name": "Garbage", "description": "Unpleasant, rotting smells from trash or waste"},
    {"name": "Pesticide", "description": "Sharp, chemical smells from pesticides or herbicides"},
    {"name": "Moldy", "description": "Musty, damp smells from mold or mildew"},
    {"name": "Paint", "description": "Strong, chemical odors from paint or solvents"},
    {"name": "Petroleum", "description": "Oily, fuel-like smells from petroleum products"},
    {"name": "Gas", "description": "Sharp, distinctive smells from natural gas or propane"},
]


def populate_smell_types():
    for smell_type in smell_types:
        # Check if the smell type already exists in the database
        existing_smell_type = SmellType.query.filter_by(name=smell_type['name']).first()

        if existing_smell_type is None:
            # If the smell type doesn't exist, create a new SmellType object and add it to the database
            new_smell_type = SmellType(name=smell_type['name'], description=smell_type['description'])
            db.session.add(new_smell_type)

    # Commit the new smell types to the database
    db.session.commit()
    print("Smell types have been added to the database.")

with app.app_context():
    populate_smell_types()
