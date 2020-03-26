from app import app
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    login_required,
    logout_user,
    current_user,
)
from models import Admin

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "admin_login"


@login_manager.user_loader
def load_user(id):
    return Admin.query.get(int(id))
