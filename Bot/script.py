from Bot.bot import bot
import utils
import datetime
from recordControl import RecordControl

user_dict = {}
recorder = RecordControl()


# ------------------ Сценарий записи -----------------
# ------------------ Сценарий записи -----------------

class Appointment:
    def __init__(self, name):
        self.name = name
        self.time = None
        self.day = None
        self.phone = None
        self.temp = None


def appointment(message):
    msg = bot.reply_to(message, "Давай записываться, как тебя зовут?")
    bot.register_next_step_handler(msg, process_name_step)
    # bot.register_next_step_handler(msg, lambda m: process_name_step(m, message.text))


def process_name_step(message):
    try:
        chat_id = message.chat.id
        name = message.text
        user = Appointment(name)
        user.temp = recorder.getMFCsDict()
        user_dict[chat_id] = user
        msg = bot.send_message(message.chat.id, "Давай выбирать МФЦ.",
                               reply_markup=utils.generate_mfc_markup(user.temp))
        bot.register_next_step_handler(msg, process_MFC_step)
    except Exception as e:
        bot.reply_to(message, 'Упс :(')


def process_MFC_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.MFC = message.text
        user.temp = user.temp.get(message.text)
        recorder.initializeFreeDates(user.temp)
        user.temp = user.temp.getChildrens()
        # print(MFCButton.getChildrens())
        msg = bot.send_message(message.chat.id, "Давай выбирать день.",
                               reply_markup=utils.generate_date_markup(user.temp))
        bot.register_next_step_handler(msg, process_day_step)
    except Exception as e:
        bot.reply_to(message, 'Упс :(')


def process_day_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.day = message.text
        for i in user.temp:
            if i.display()[:-3:-1] == message.text[:2][::-1]:
                user.temp = i.getChildrens()
                break
        msg = bot.send_message(message.chat.id, "Отлично, выбираем время.",
                               reply_markup=utils.generate_time_markup(user.temp))
        # генерирую клаву
        bot.register_next_step_handler(msg, process_time_step)
    except:
        bot.reply_to(message, 'Упс :(')


def process_time_step(message):
    chat_id = message.chat.id
    try:
        time = datetime.datetime.strptime(message.text, '%H:%M')
        user = user_dict[chat_id]
        user.time = time
        msg = bot.reply_to(message, "Остался последний шаг, запишем номер телефона")
        bot.register_next_step_handler(msg, process_phone_step)
    except:
        msg = bot.send_message(message.chat.id, "Нажимай кнопку, а не пиши сам.")
        # генерирую клаву
        bot.register_next_step_handler(msg, process_time_step)


def process_phone_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        if utils.check_phone(message.text):
            user.phone = message.text
            bot.reply_to(message, f"Ты записан!\nИмя: {user.name}\nВремя: {user.time.strftime('%H:%M')}\n"
                                  f"День: {user.day}\nТелефон: {user.phone}")

            recorder.makeEntry(buttonTime=user.time, dateButton=user.day, MFCButton=user.MFC,
                               name=user.name, surname=user.phone,
                               username=chat_id)
        else:
            msg = bot.reply_to(message, "Меня не проведешь, вводи настоящий номер!")
            bot.register_next_step_handler(msg, process_phone_step)
    except Exception as e:
        bot.reply_to(message, 'Упс :(')


bot.polling()
