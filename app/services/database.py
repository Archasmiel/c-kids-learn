from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def register(app: Flask):
    db.init_app(app)
