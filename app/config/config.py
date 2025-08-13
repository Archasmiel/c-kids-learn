from pathlib import Path
from dotenv import load_dotenv
import secrets, os

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
    APP_PATH = Path(os.path.dirname(__file__)).parent
    PROJECT_PATH = APP_PATH.parent
    STATIC_PATH = PROJECT_PATH / os.getenv('STATIC_PATH', 'static')
    TEMPLATE_PATH = PROJECT_PATH / os.getenv('TEMPLATE_PATH', 'templates')
    INSTANCE_PATH = PROJECT_PATH / os.getenv('INSTANCE_PATH', 'instance')
    MIGRATIONS_PATH = PROJECT_PATH / os.getenv('MIGRATIONS_PATH', 'migrations')

    DB_PATH = INSTANCE_PATH / SQLALCHEMY_DATABASE_URI.split('/')[-1]
    TOOLS_PATH = PROJECT_PATH / os.getenv('TOOLS_PATH', 'tools')
    LESSONS_PATH = PROJECT_PATH / os.getenv('LESSONS_PATH', 'lessons')
    PYTHON_EXE = PROJECT_PATH / os.getenv('PYTHON_EXE', '')

    # ----- Backup -----
    BACKUP_PATH = PROJECT_PATH / os.getenv('BACKUP_PATH', 'backup')
    BACKUP_INTERVAL = int(os.getenv('BACKUP_INTERVAL_SEC', 300))

    # ----- Compiler tool -----
    RUNNER_CFG = {
        "COMPILER": os.getenv('RUNNER_COMPILER', 'gcc'),
        "TCC_PATH": TOOLS_PATH / os.getenv('RUNNER_TCC_PATH', ''),
        "GCC_PATH": TOOLS_PATH / os.getenv('RUNNER_GCC_PATH', ''),
        "TIMEOUT_SEC": int(os.getenv('RUNNER_TIMEOUT_SEC', 3))
    }


class DevConfig(BaseConfig):
    DEBUG = 1

class ProdConfig(BaseConfig):
    DEBUG = 0