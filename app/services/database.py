from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from ..config import current_cfg as cfg
from .logger import logger

db = SQLAlchemy()


def register(app: Flask):
    cfg.INSTANCE_PATH.mkdir(parents=True, exist_ok=True)
    logger.info('Checked backup dir for existance.')

    db.init_app(app)