from flask_sqlalchemy import SQLAlchemy

# Initialize the db with the app directly
db = SQLAlchemy()  

def initialize_database(app):
    with app.app_context():
        db.create_all()