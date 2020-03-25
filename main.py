"""Start point for the app"""

from app import app, db
from routes import *
from models import *

if __name__ == "__main__":
    """run app and make migrations"""
    db.create_all()
    app.run()
