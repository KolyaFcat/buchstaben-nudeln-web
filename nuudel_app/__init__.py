import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

class GameFlask(Flask):
    game: 'Nuudel_game'  # type: ignore Type hint for the game instance

def create_app():
    template_path = os.path.join(os.path.dirname(__file__), 'templates')
    static_path = os.path.join(os.path.dirname(__file__), 'static')
    print(f"Template path: {template_path}")
    app = GameFlask(__name__, 
                template_folder=template_path, 
                static_folder=static_path,
                instance_relative_config=True)
    app.config.from_object(Config)
    print('SQLALCHEMY_DATABASE_URI:', Config.SQLALCHEMY_DATABASE_URI)
    db.init_app(app)

    with app.app_context():
        from . import models  # Import models to register them with the app

        db.create_all()  # Create database tables
        print("DB created or already exists")

        from nuudel_app.nuudel_game import Nuudel_game
        app.game = Nuudel_game()  # Initialize the game instance

    return app