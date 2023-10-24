import pytz
from datetime import datetime
from database import db

# Create a user model that represents user table in our database

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    messages = db.relationship('Message', backref='author', lazy='joined')

# Create a message model that represents user table in our database

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(pytz.timezone('EET')))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)