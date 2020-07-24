from spa.views import main
from flask import current_app


def register_frontend_views():
    current_app.register_blueprint(main.bp)
