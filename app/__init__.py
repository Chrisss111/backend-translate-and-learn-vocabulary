from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "SQLALCHEMY_DATABASE_URI")

    # Import models here for Alembic setup
    # from app.models.ExampleModel import ExampleModel
    from app.models.vocablist import Vocablist
    from app.models.word import Word
   

    # Setup DB
    db.init_app(app)
    migrate.init_app(app, db)
    

    # Register Blueprints here
    from .routes import vocablists_bp
    app.register_blueprint(vocablists_bp)

    from .routes import words_bp
    app.register_blueprint(words_bp)

    from .routes import translation_bp
    app.register_blueprint(translation_bp)

    CORS(app)
    return app
