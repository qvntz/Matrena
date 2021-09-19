from telebot import types
import re
from DB.Tools import get_data_from_str
import random


def generate_mfc_markup(MFCButtons):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    markup.add("Главное меню")
    markup.add("Назад")
    for MFC in MFCButtons:
        markup.add(MFC)
    return markup


def generate_date_markup(DateButtons):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    for button in DateButtons:
        markup.add(get_data_from_str(button.display()))
    markup.add("Назад")
    markup.add("Главное меню")
    return markup


def generate_time_markup(TimeButtons):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=5)
    for button in TimeButtons:
        markup.add(button.display())
    markup.add("Назад")
    markup.add("Главное меню")
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
    return generate_markup(["Популярные вопросы", "Запись на консультацию",
                            "Ближайший МФЦ", "Проверить запись"])


def error_message():
    message = ["Упс, что-то пошло не так\nВерну Вас в главное меню :(",
               "Голова болит, забыла что мы делали, давайте попробуем еще раз\nВозвращаю в главное меню",
               "А может не будем этим заниматься, а посмотрим, что еще я умею?\nПеревожу в главное меню",
               "Ой-ой, где-то накосячила. Вызываю спасателей\nЛетим в главное меню!!"]

    return random.choice(message)