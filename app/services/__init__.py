import os
from importlib import import_module

from flask import Flask
from .logger import logger
from ..config import current_cfg as cfg

db_path = cfg.INSTANCE_DIR / 'app.db'


def register(app: Flask):
    cfg.INSTANCE_DIR.mkdir(exist_ok=True, parents=True)
    cfg.BACKUP_DIR.mkdir(exist_ok=True, parents=True)

    current_dir = os.path.dirname(__file__)

    for filename in os.listdir(current_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = f'{__name__}.{filename[:-3]}'
            module = import_module(module_name)

            register_func = getattr(module, "register", None)
            if callable(register_func):
                register_func(app)
                logger.info(f'Registered \'{module_name}\' service')
