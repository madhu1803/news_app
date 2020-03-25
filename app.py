"""Config for the app | flask app is configured here"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

project_dir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
app.debug = True
app.secret_key = "secret"
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"sqlite:///{os.path.join(project_dir, 'database.db')}"

db = SQLAlchemy(app)
