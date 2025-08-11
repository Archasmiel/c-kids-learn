from flask import Flask
from pathlib import Path
import secrets

def create_app():
    app = Flask(__name__, 
                instance_relative_config=True,
                static_folder="../static",
                template_folder="../templates")
    app.config.update(
        SECRET_KEY=secrets.token_hex(32),
        SQLALCHEMY_DATABASE_URI="sqlite:///app.db",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        RUNNER_CFG={
            "COMPILER": "tcc",  # tcc or gcc
            "TCC_PATH": str(Path(app.root_path).parent / "tools" / "tcc" / "tcc.exe"),
            "GCC_PATH": "gcc",  # later if install MinGW
            "TIMEOUT_SEC": 3
        }
    )

    Path(app.instance_path).mkdir(parents=True, exist_ok=True)

    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app