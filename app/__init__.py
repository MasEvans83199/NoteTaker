from flask import Flask
from .database import db
from .routes import bp as notes_bp

def create_app(config_filename):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)
    db.init_app(app)
    app.register_blueprint(notes_bp)
    return app
