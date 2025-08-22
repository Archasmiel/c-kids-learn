from flask import Flask
from flask_login import LoginManager
from .database import db
from ..config import current_cfg as cfg
from ..models.user import User

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id: str):
    return db.session.get(User, int(user_id))


def register(app: Flask):
    login_manager.login_view = cfg.LOGIN_VIEW
    login_manager.login_message = 'Для доступу треба увійти'
    login_manager.login_message_category = cfg.LOGIN_MSG_CATEGORY
    login_manager.init_app(app)
