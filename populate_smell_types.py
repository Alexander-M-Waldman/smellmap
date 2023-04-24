from app import create_app, db
from app.models import SmellType

app = create_app()


# Define a list of smell types to be added to the database
smell_types = [
    {"name": "Sweet", "description": "Pleasant, sugary smells", "color": "#FFD700"},
    {"name": "Sour", "description": "Sharp, acidic smells", "color": "#FF4500"},
    {"name": "Salty", "description": "Sea-like or mineral smells", "color": "#1E90FF"},
    {"name": "Bitter", "description": "Harsh, acrid smells", "color": "#8B0000"},
    {"name": "Earthy", "description": "Soil-like or damp smells", "color": "#8B4513"},
    {"name": "Fruity", "description": "Fresh, fruity smells", "color": "#32CD32"},
    {"name": "Floral", "description": "Sweet, flowery smells", "color": "#FF69B4"},
    {"name": "Spicy", "description": "Strong, peppery smells", "color": "#FF6347"},
    {"name": "Woody", "description": "Resinous, bark-like smells", "color": "#A0522D"},
    {"name": "Chemical", "description": "Pungent, synthetic smells", "color": "#778899"},
    {"name": "Smoky", "description": "Burnt, acrid smells from smoke or fires", "color": "#696969"},
    {"name": "Industrial", "description": "Heavy, oily smells from factories or machinery", "color": "#808080"},
    {"name": "Sewage", "description": "Foul, unpleasant odors from sewage or waste", "color": "#483D8B"},
    {"name": "Exhaust", "description": "Pungent, acrid smells from vehicle exhaust", "color": "#2F4F4F"},
    {"name": "Garbage", "description": "Unpleasant, rotting smells from trash or waste", "color": "#6B8E23"},
    {"name": "Pesticide", "description": "Sharp, chemical smells from pesticides or herbicides", "color": "#FFA07A"},
    {"name": "Moldy", "description": "Musty, damp smells from mold or mildew", "color": "#708090"},
    {"name": "Paint", "description": "Strong, chemical odors from paint or solvents", "color": "#B22222"},
    {"name": "Petroleum", "description": "Oily, fuel-like smells from petroleum products", "color": "#FF7F50"},
    {"name": "Gas", "description": "Sharp, distinctive smells from natural gas or propane", "color": "#DC143C"},
]


def populate_smell_types():
    for smell_type in smell_types:
        # Check if the smell type already exists in the database
        existing_smell_type = SmellType.query.filter_by(name=smell_type['name']).first()

        if existing_smell_type is None:
            # If the smell type doesn't exist, create a new SmellType object and add it to the database
            new_smell_type = SmellType(name=smell_type['name'], description=smell_type['description'], color=smell_type["color"])
            db.session.add(new_smell_type)

    # Commit the new smell types to the database
    db.session.commit()
    print("Smell types have been added to the database.")

with app.app_context():
    populate_smell_types()
