from flask import Flask
from flask_migrate import Migrate
from flask_migrate import init as mig_init, migrate as mig_migrate, upgrade as mig_upgrade
from .database import db
from ..config import current_cfg as cfg
from .logger import logger
import os

migrate = Migrate()


def check_db_exist():
    mig_str = str(cfg.MIGRATIONS_PATH)

    if os.path.exists(cfg.DB_PATH):
        logger.info('Database file exists, skipping creation.')
    else:
        logger.warning('Database file absent, creating...')
    
    logger.info('Running migrations...')
    if not os.path.exists(cfg.MIGRATIONS_PATH):
        mig_init(mig_str)

    from secrets import token_hex
    mig_migrate(mig_str, token_hex(32))
    mig_upgrade(mig_str)


def register(app: Flask):
    migrate.init_app(app, db)

    with app.app_context():
        check_db_exist()
