from flask import Flask, request, redirect, url_for, current_app

from config import Config




def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)


    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.distance import bp as distance_bp
    app.register_blueprint(distance_bp)

    return app


