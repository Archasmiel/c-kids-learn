from flask import Flask, request, session
from flask_babel import Babel
from ..config import current_cfg as cfg

babel = Babel()


def get_locale():
    lang = request.args.get("lang") or session.get("lang")
    if lang and lang in cfg.BABEL_SUPPORTED_LOCALES:
        session["lang"] = lang
        return lang

    return request.accept_languages.best_match(cfg.BABEL_SUPPORTED_LOCALES) \
        or cfg.BABEL_DEFAULT_LOCALE


def get_timezone():
    return session.get("timezone", cfg.BABEL_DEFAULT_TIMEZONE)


def register(app: Flask):
    babel.init_app(
        app=app,
        default_locale=cfg.BABEL_DEFAULT_LOCALE,
        default_timezone=cfg.BABEL_DEFAULT_TIMEZONE,
        locale_selector=get_locale,
        timezone_selector=get_timezone
    )

    @app.context_processor
    def inject_get_locale():
        return dict(get_locale=get_locale)
