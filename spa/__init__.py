from flask import Flask
from spa.views import register_frontend_views


def create_app():
    app = Flask(__name__)
    app.config["ENV"] = "development"

    with app.app_context():
        register_frontend_views()

    return app
