from telebot import types
import re
from DB.Tools import get_data_from_str


def generate_mfc_markup(MFCButtons):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    for MFC in MFCButtons:
        markup.add(MFC)
    return markup


def generate_date_markup(DateButtons):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    for button in DateButtons:
        markup.add(get_data_from_str(button.display()))
    return markup


def generate_time_markup(TimeButtons):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=5)
    for button in TimeButtons:
        markup.add(button.display())
    return markup


def check_phone(num: str):  # 88005553535
    if len(num) == 11 and num[0] == "8" or len(num) == 12 and num[0] == "+":
        clear_phone = re.sub(r'\D', '', num)
        result = re.match(r'^[78]?\d{10}$', clear_phone)
        return bool(result)
    return False


def generate_markup(buttons, width=1, mainMenu=None):
    """
    Создаем кастомную клавиатуру для выбора ответа
    :param buttons: List кнопок
    :return: Объект кастомной клавиатуры
    """

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=width)
    markup.add(*buttons)
    if mainMenu is not None:
        markup.add("Главное меню")
    return markup


def generate_mainMenu_markup():
    return generate_markup(["Популярные вопросы", "Запись на консультацию", "Ближайший МФЦ"])
