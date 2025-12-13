import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app():
    template_path = os.path.join(os.path.dirname(__file__), 'templates')
    static_path = os.path.join(os.path.dirname(__file__), 'static')
    print(f"Template path: {template_path}")
    app = Flask(__name__, 
                template_folder=template_path, 
                static_folder=static_path,
                instance_relative_config=True)
    app.config.from_object(Config)
    print('SQLALCHEMY_DATABASE_URI:', Config.SQLALCHEMY_DATABASE_URI)
    db.init_app(app)

    with app.app_context():
        from . import models  # Import models to register them with the app
        from .nuudel_game import Nuudel_game

        db.create_all()  # Create database tables
        animals = [
            "Hund", "Katze", "Pferd", "Kuh", "Schwein",
            "Schaf", "Ziege", "Huhn", "Ente", "Gans",
            "Tiger", "Löwe", "Wolf", "Bär", "Hase",
            "Elch", "Eichhörnchen", "Elefant", "Giraffe"
        ]

        tools = [
            "Hammer", "Schraubenzieher", "Säge", "Brecheisen", "Zange",
            "Akkuschrauber", "Bohrmaschine", "Stechbeitel", "Hobel",
            "Feile", "Messschieber", "Stemmeisen", "Lötkolben",
            "Metallsäge", "Wasserwaage", "Maßband"
        ]

        kitchen_items = [
            "Topf", "Pfanne", "Wasserkocher", "Teller", "Tasse",
            "Löffel", "Gabel", "Messer", "Schüssel",
            "Reibe", "Schöpflöffel", "Sieb", "Kühlschrank", "Backofen",
            "Herd", "Mikrowelle", "Mixer"
        ]
        gm = Nuudel_game()

        gm.clean_table_category_word()  # Очиистка таблиц
        print(gm.update_category("animals", "easy"))
        print(gm.update_category("kitchen", "medium"))
        print(gm.update_category("tools", "hard"))
        print(gm.update_word(animals, "animals"))
        print(gm.update_word(tools, "tools"))
        print(gm.update_word(kitchen_items, "kitchen"))
        print("DB created or already exists")

    return app
