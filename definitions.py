from enum import Enum
from os import path


# Разметка COMPLETED_FAQ_FILE используется в DataFrame
class DF(Enum):
    QUESTION = "Вопрос"
    METHOD = "Способ"
    DOCS = "Документы"
    ACTIONS = "Порядок действий"
    LINK = "Ссылка"


# Константа корневая папка проекта
ROOT_DIR = path.dirname(path.abspath(__file__))

# Константа папка с данными
DATA_DIR = path.join(ROOT_DIR, "data")

# Json для кнопок
JSON_BUTTONS_FILE = path.join(DATA_DIR, "answers.json")

# Данные для обучения
LEARNING_DATA_FILE = path.join(DATA_DIR, "learning_data.csv")

# Законченный файл с ответами
COMPLETED_FAQ_FILE = path.join(DATA_DIR, "data.csv")
