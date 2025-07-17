from nuudel_app import db, create_app
from nuudel_app.models import Word, Category

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
        category_obj = Category.query.filter_by(category=category).first()
        if not category_obj or not category_obj.words:
            return None
        words_lst = [word.word for word in category_obj.words]
        return 'ГИРТ'

    def check_answer(self, answer_str):
        """
        input:
            answer_str: str, ответ пользователя

        output:
            score: int/None
        """
        return 100
    
    def add_list_of_words(self, words_list, category):
        """
        input:
            words_list: list of str, список слов для добавления в базу
            category: str, категория для слов

        output:
            None
        """
        category_obj = Category.query.filter_by(category=category).first()
        if not category_obj:
            category_obj = Category(category=category)
            db.session.add(category_obj)
            db.session.commit()

        existing_words = {word.word for word in category_obj.words}
        
        for word in words_list:
            if word not in existing_words:
                word_data = Word(word=word, category_ref=category_obj)
                db.session.add(word_data)
        db.session.commit()

    def delete_category_and_words(self, category):
        """
        input:
            category: str, категория для удаления, при этом все слова в этой категории будут удалены

        output:
            None
        """
        category_obj = Category.query.filter_by(category=category).first()
        if category_obj:
            db.session.delete(category_obj)
            db.session.commit() 

        else:
            raise ValueError(f"Категория '{category}' не найдена в базе данных.")
        
    def delete_word(self, word):
        """
        input:
            word: str, слово для удаления

        output:
            None
        """
        word_obj = Word.query.filter_by(word=word).first()
        if word_obj:
            db.session.delete(word_obj)
            db.session.commit()
        else:
            raise ValueError(f"Слово '{word}' не найдено в базе данных.")

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
        # app.game.delete_category_and_words("animals")
        app.game.add_list_of_words(animals, "animals")

        app.game.delete_word("тигр")