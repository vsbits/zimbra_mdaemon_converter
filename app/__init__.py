from flask import Flask
from .blueprints import blp
from .config import SECRET_KEY


def create_app() -> Flask:

    app = Flask(__name__)
    app.secret_key = SECRET_KEY

    app.register_blueprint(blp)

    return app
