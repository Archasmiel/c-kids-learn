import os
from importlib import import_module

from flask import Flask, Blueprint
from ..services.logger import logger


def register(app: Flask):
    current_dir = os.path.dirname(__file__)

    for filename in os.listdir(current_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = f'{__name__}.{filename[:-3]}'
            module = import_module(module_name)

            bp = getattr(module, "bp", None)
            if isinstance(bp, Blueprint):
                app.register_blueprint(bp)
                logger.info(f'Registered \'{module_name}\' routes')
