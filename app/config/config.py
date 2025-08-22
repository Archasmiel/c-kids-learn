import os
import secrets
from pathlib import Path

from dotenv import load_dotenv


class BaseConfig:
    load_dotenv()

    # ----- Secrets -----
    SECRET_KEY = secrets.token_hex(32)

    # ----- Database ------
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = (os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', 0) == 1)

    # ----- Login -----
    LOGIN_VIEW = os.getenv('LOGIN_VIEW', 'auth.login')
    LOGIN_MSG_CATEGORY = os.getenv('LOGIN_MSG_CATEGORY', 'info')

    # ----- Base paths -----
    APP_DIR = Path(os.path.dirname(__file__)).parent
    PROJECT_DIR = APP_DIR.parent
    STATIC_DIR = PROJECT_DIR / os.getenv('STATIC_PATH', 'app/static')
    TEMPLATE_DIR = PROJECT_DIR / os.getenv('TEMPLATE_PATH', 'app/templates')
    TRANSLATIONS_DIR = PROJECT_DIR / os.getenv('TRANSLATIONS_PATH', 'app/translations')

    INSTANCE_DIR = PROJECT_DIR / os.getenv('INSTANCE_PATH', 'instance')
    MIGRATIONS_DIR = PROJECT_DIR / os.getenv('MIGRATIONS_PATH', 'migrations')
    TOOLS_DIR = PROJECT_DIR / os.getenv('TOOLS_PATH', 'tools')
    LESSONS_DIR = PROJECT_DIR / os.getenv('LESSONS_PATH', 'lessons')
    PYTHON_EXE = PROJECT_DIR / os.getenv('PYTHON_EXE', '')

    # ----- Backup -----
    BACKUP_DIR = PROJECT_DIR / os.getenv('BACKUP_PATH', 'backup')
    BACKUP_INTERVAL = int(os.getenv('BACKUP_INTERVAL_SEC', 300))

    # ----- Compiler tool -----
    RUNNER_CFG = {
        "COMPILER": os.getenv('RUNNER_COMPILER', 'gcc'),
        "TCC_PATH": TOOLS_DIR / os.getenv('RUNNER_TCC_PATH', ''),
        "GCC_PATH": TOOLS_DIR / os.getenv('RUNNER_GCC_PATH', ''),
        "TIMEOUT_SEC": int(os.getenv('RUNNER_TIMEOUT_SEC', 3))
    }

    # ----- Translations -----
    BABEL_DEFAULT_LOCALE = os.getenv('BABEL_DEFAULT_LOCALE', 'uk')
    BABEL_SUPPORTED_LOCALES = os.getenv('BABEL_SUPPORTED_LOCALES', ['en', 'uk'])
    BABEL_DEFAULT_TIMEZONE = os.getenv('BABEL_DEFAULT_TIMEZONE', 'UTC')


class DevConfig(BaseConfig):
    DEBUG = 1


class ProdConfig(BaseConfig):
    DEBUG = 0
