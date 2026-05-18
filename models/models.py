from extensions import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    gardens = db.relationship('Garden', backref='owner', lazy=True, cascade='all, delete-orphan')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Garden(db.Model):
    __tablename__ = 'gardens'

    garden_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(200), nullable=True)

    plants = db.relationship('Plant', backref='garden', lazy=True, cascade='all, delete-orphan')


class Plant(db.Model):
    __tablename__ = 'plants'

    plant_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    garden_id = db.Column(db.Integer, db.ForeignKey('gardens.garden_id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(100), nullable=True)
    planted_date = db.Column(db.Date, nullable=True)
    notes = db.Column(db.Text, nullable=True)

    logs = db.relationship('GrowthLog', backref='plant', lazy=True, cascade='all, delete-orphan')
    reminders = db.relationship('Reminder', backref='plant', lazy=True, cascade='all, delete-orphan')


class GrowthLog(db.Model):
    __tablename__ = 'growth_logs'

    log_id = db.Column(db.Integer, primary_key=True)
    plant_id = db.Column(db.Integer, db.ForeignKey('plants.plant_id'), nullable=False)
    height = db.Column(db.Float, nullable=True)
    leaf_count = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    recorded_at = db.Column(db.DateTime, default=datetime.utcnow)


class Reminder(db.Model):
    __tablename__ = 'reminders'

    reminder_id = db.Column(db.Integer, primary_key=True)
    plant_id = db.Column(db.Integer, db.ForeignKey('plants.plant_id'), nullable=False)
    reminder_type = db.Column(db.String(50), default='watering')
    due_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), default='pending')