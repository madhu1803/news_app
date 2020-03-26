"""Contains the DB models"""

from app import db
import datetime
from flask_login import UserMixin


class Admin(UserMixin, db.Model):
    """Admin model"""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, nullable=False
    )


class Post(db.Model):
    """Posts model"""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    subtitle = db.Column(db.String(300), nullable=False)
    content = db.Column(db.String(1000), nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, nullable=False
    )
