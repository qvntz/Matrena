import telebot
import config
from utils import generate_markup
import script
from arсhive import finder_mfc
bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def greet(message):
    bot.reply_to(message, "Привет :)\nЯ еще немножко глупенькая 😅, НО ТЫ НЕ ПУГАЙСЯ!!!!"
                          "\nЯ учусь и скоро буду очень умной ( круче всех😎😎😎 )"
                          "\nА пока ты можешь мне помочь, узнав то, что тебя интересует ☺️☺️☺️")


@bot.message_handler(content_types=["text"])
def answer(message):
    if "ближайший мфц" == message.text.lower():
        keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        button_geo = telebot.types.KeyboardButton(text="Отправить местоположение", request_location=True)
        keyboard.add(button_geo)
        bot.send_message(message.chat.id, "Для этого Вам нужно нажать на кнопку"
                                          " и отправить мне свое местоположение",
                         reply_markup=keyboard)
    elif "запись на консультацию" == message.text.lower():
        script.appointment(message)  # сценарий записи
    elif "госуслуги" == message.text.lower():
        keyboard = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton(text="Перейти на Госуслуги", url="https://www.gosuslugi.ru/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Я прикрепил снизу все ссылки, чтобы тебе было удобнее.",
                         reply_markup=keyboard)
    else:
        pass
        # bot.send_message(message.chat.id, message.text, reply_markup=generate_markup(message.text.split()))


@bot.message_handler(content_types=["location"])
def location(message):
    if message.location is not None:
        bot.send_message(message.chat.id,
                         f"Ближайший офис МФЦ - "
                         f"{finder_mfc(message.location.latitude, message.location.longitude)}")


if __name__ == "__main__":
    bot.infinity_polling()
