from flask import Flask

def create_app():
    from .config import DevConfig as cfg
    app = Flask(__name__, 
                template_folder=cfg.TEMPLATE_PATH,
                static_folder=cfg.STATIC_PATH)
    app.config.from_object(cfg)

    from .services import register as register_services
    register_services(app)

    from .routes import register as register_routes
    register_routes(app)

    return app