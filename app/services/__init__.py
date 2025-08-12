from flask import Flask
from importlib import import_module
import os


def register(app: Flask):
    current_dir = os.path.dirname(__file__)

    for filename in os.listdir(current_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = f'{__name__}.{filename[:-3]}'
            module = import_module(module_name)

            register = getattr(module, "register", None)
            if callable(register):
                register(app)
                print(f'> Registered \'{module_name}\' service')