from sqlalchemy import text
from nuudel_app import db, create_app
from nuudel_app.models import Word, Category
import random

class Nuudel_game():
    def __init__(self):
        self.db = db
        self.word = None
        self.category = None
        self.nuudel_word = None

    def get_nuudel_word(self, category):
        """
        input:
            category: str категория для nuudel_word

        output:
            nuudel_word: str
        """
        self.category = category
        try:
            category_id = Category.query.filter_by(category=self.category).first()
            if not category_id:
                return "error: Not_category"
        except Exception as e:
            print(f"Ошибка при поиске категории: {e}")
            return "error: Not_category"
        
        word = Word.query.filter_by(category_id=category_id.id).order_by(self.db.func.random()).first()
        if not word:
            return "error: Not_word"
        
        self.word = word.word
        print(self.word)
        self.nuudel_word = ''.join(random.sample(self.word, len(self.word)))
        return self.nuudel_word

    def update_category(self, category_input, difficulty):    
        existing = Category.query.filter_by(category=category_input).first()
        if existing:
            return "update_category status: Категория уже существует"
        category = Category(category=category_input, difficulty=difficulty)
        self.db.session.add(category)
        self.db.session.commit()
        return "update_category status: success"
    
    def update_word(self, wors, category_save):
        category = Category.query.filter_by(category=category_save).first()
        if not category:
            return f"Категория {category_save} не найдена"

        update_wors = 0

        for w in wors:
            existing_word = Word.query.filter_by(word=w, category_id=category.id).first()
            if not existing_word:
                word_data = Word(word=w, category_ref=category)
                self.db.session.add(word_data)
                update_wors += 1
        self.db.session.commit()
        return f"update_word status: success  update_wors: {update_wors}"
    
    def clean_table_category_word(self):
        self.db.session.execute(text("TRUNCATE TABLE word, category CASCADE")) 
        self.db.session.commit()
    
if __name__ == "__main__":
    app = create_app()
    with app.app_context():        
        animals = [
            "собака", "кошка", "лошадь", "корова", "свинья",
            "овца", "коза", "курица", "утка", "гусь",
            "тигр", "лев", "волк", "медведь", "заяц",
            "лось", "белка", "слон", "жираф"
        ]
        tools = [
            "молоток", "отвёртка", "пила", "гвоздодёр", "пассатижи",
            "шуруповёрт", "дрель", "стаместка", "рубанок",
            "напильник", "штангенциркуль", "лом", "паяльник",
            "ножовка", "уровень", "рулетка"
        ]
        kitchen_items = [
            "кастрюля", "сковорода", "чайник", "тарелка", "чашка",
            "ложка", "вилка", "нож", "миска",
            "терка", "половник", "дуршлаг", "холодильник", "духовка",
            "плита", "микроволновка", "блендер"
        ]
        gm = Nuudel_game()
        print(gm.update_category("animals", "easy"))
        print(gm.update_category("kitchen", "medium"))
        print(gm.update_category("tools", "hard"))
        print(gm.update_word(animals, "animals"))
        print(gm.update_word(tools, "tools"))
        print(gm.update_word(kitchen_items, "kitchen"))
        # game = Nuudel_game()
        # print(game.get_nuudel_word("animals"))