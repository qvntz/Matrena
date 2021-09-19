import telebot
import config
import script
from arсhive.finder_mfc import finder_mfc
from Bot.responder import get_answer
import utils
from DB.FuctionsDB import getRecordByUsername
from recordControl import RecordControl
from Answerer.spellCheck import spellCheck

bot = telebot.TeleBot(config.token)
step = 0

# from DB.MakeDB import delete_DB, Base, engine, post_MFC
# Base.metadata.create_all(bind=engine)
# post_MFC()


@bot.message_handler(commands=['start'])
def greet(message):
    bot.send_message(message.chat.id, "Привет :)\nЯ еще немножко глупенькая 😅, НО ТЫ НЕ ПУГАЙСЯ!!!!"
                                      "\nЯ учусь и скоро буду очень умной ( круче всех😎😎😎 )"
                                      "\nА пока ты можешь мне помочь, узнав то, что тебя интересует ☺️☺️☺️",
                     reply_markup=utils.generate_mainMenu_markup())


@bot.message_handler(commands=['help'])
def info(message):
    bot.reply_to(message, "Тыкай на кнопки или пиши текстом)")


@bot.message_handler(content_types=["text"])
def answer(message):
    current_text = spellCheck(message.text.lower())
    if "главное меню" == current_text:
        bot.send_message(message.chat.id, "Переключаю на главное меню..", reply_markup=utils.generate_mainMenu_markup())

    elif "проверить запись" == current_text:
         record = RecordControl()
         temp = record.getInfoAboutRecordByChatID(chatID=message.chat.id)
         if temp:
             bot.send_message(message.chat.id, f"Проверила запись 😁\nВы записаны в {temp[2]} \n{temp[1]} на {temp[0]} 🥳🥳🥳0",
                              reply_markup=utils.generate_mainMenu_markup())
         else:
             bot.send_message(message.chat.id, "Вы еще не записаны", reply_markup=utils.generate_mainMenu_markup())

    elif "ближайший мфц" == current_text:
        keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        button_geo = telebot.types.KeyboardButton(text="Отправить местоположение", request_location=True)
        keyboard.add(button_geo)
        bot.send_message(message.chat.id, "Для этого Вам нужно нажать на кнопку"
                                          " и отправить мне свое местоположение",
                         reply_markup=keyboard)
    elif "популярные вопросы" == current_text:
        bot.send_message(message.chat.id, "Самые популярные категории на данный момент",
                         reply_markup=utils.generate_markup(["Паспорт", "СНИЛС", "Запись на консультацию",
                                                             "Ближайший МФЦ"], 2, mainMenu=True))

    elif "запись на консультацию" == current_text:
        script.appointment(message)  # сценарий записи

    elif "госуслуги" == current_text:
        keyboard = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton(text="Перейти на Госуслуги", url="https://www.gosuslugi.ru/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Я прикрепил снизу все ссылки, чтобы тебе было удобнее.",
                         reply_markup=keyboard)

    else:
        try:
            get_answer(message, bot)
        except Exception as e:
            print(e)


@bot.message_handler(content_types=["location"])
def location(message):
    if message.location is not None:
        bot.send_message(message.chat.id,
                         f"Ближе всего к Вам: \n{finder_mfc(message.location.latitude, message.location.longitude)}",
                         reply_markup=utils.generate_mainMenu_markup())


if __name__ == "__main__":
    bot.infinity_polling()
