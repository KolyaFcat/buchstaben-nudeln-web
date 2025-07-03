from nuudel_app import db, create_app
from nuudel_app.models import Word

class Nuudel_game():
    def __init__(self):
        self.db = db

    def get_nuudel_word(self, category):
        """
        input:
            category: str категория для nuudel_word

        output:
            nuudel_word: str
        """
        return 'ГИРТ'

    def check_answer(self, answer_str):
        """
        input:
            answer_str: str, ответ пользователя

        output:
            score: int/None
        """
        return 100

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        animals = [
            "тигр",
            "лев",
            "слон",
            "зебра",
            "волк",
            "медведь",
            "лисица",
            "кенгуру",
            "жираф",
            "панда"
        ]
        for w in animals:
            word_data = Word(word=w, category="animals")
            db.session.add(word_data)
        db.session.commit()