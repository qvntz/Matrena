from Bot.bot import bot
import Bot.utils as utils
import datetime
from recordControl import RecordControl
from DB.Tools import get_datetime_from_data
from DB.UpdateDB import delete_past_time_by_name


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
    msg = bot.reply_to(message, "Давай записываться, как тебя зовут?",
                       reply_markup=utils.generate_markup(["Главное меню"]))
    bot.register_next_step_handler(msg, process_name_step)
    # bot.register_next_step_handler(msg, lambda m: process_name_step(m, message.text))


def process_name_step(message):
    try:
        if message.text.lower() == "главное меню":
            bot.send_message(message.chat.id, 'Перевожу!',
                             reply_markup=utils.generate_mainMenu_markup())
        else:
            chat_id = message.chat.id
            name = message.text
            user = Appointment(name)
            user.temp = recorder.getMFCsDict()
            user_dict[chat_id] = user
            msg = bot.send_message(message.chat.id, "Давай выбирать МФЦ.",
                                   reply_markup=utils.generate_mfc_markup(user.temp))
            bot.register_next_step_handler(msg, process_MFC_step)
    except Exception as e:
        bot.reply_to(message, utils.error_message())
        bot.send_message(message.chat.id, 'Вернула!', reply_markup=utils.generate_mainMenu_markup())


def process_MFC_step(message):
    try:
        if message.text.lower() == "в начало":
            msg = bot.reply_to(message, "Хорошо, давайте перезапишем Ваше имя!",
                               reply_markup=utils.generate_markup(["Главное меню"]))
            bot.register_next_step_handler(msg, process_name_step)
        elif message.text.lower() == "главное меню":
            bot.send_message(message.chat.id, 'Перевожу!',
                             reply_markup=utils.generate_mainMenu_markup())
        else:
            chat_id = message.chat.id
            user = user_dict[chat_id]
            user.MFC = message.text
            delete_past_time_by_name(user.MFC)
            user.temp = user.temp.get(message.text)
            recorder.initializeFreeDates(user.temp)
            user.temp = user.temp.getChildrens()
            # print(MFCButton.getChildrens())
            msg = bot.send_message(message.chat.id, "Давай выбирать день.",
                                   reply_markup=utils.generate_date_markup(user.temp))
            bot.register_next_step_handler(msg, process_day_step)
    except Exception as e:
        print(e)
        bot.reply_to(message, utils.error_message())
        bot.send_message(message.chat.id, 'Вернула!', reply_markup=utils.generate_mainMenu_markup())


def process_day_step(message):
    try:
        if message.text.lower() == "в начало":
            msg = bot.reply_to(message, "Хорошо, давайте перезапишем Ваше имя.",
                               reply_markup=utils.generate_markup(["Главное меню"]))
            bot.register_next_step_handler(msg, process_name_step)
        elif message.text.lower() == "главное меню":
            bot.send_message(message.chat.id, 'Перевожу!',
                             reply_markup=utils.generate_mainMenu_markup())
        else:
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
        bot.reply_to(message, utils.error_message())
        bot.send_message(message.chat.id, 'Вернула!', reply_markup=utils.generate_mainMenu_markup())


def process_time_step(message):
    chat_id = message.chat.id
    try:
        if message.text.lower() == "в начало":
            msg = bot.reply_to(message, "Хорошо, давай перезапишем Ваше имя.",
                               reply_markup=utils.generate_markup(["Главное меню"]))
            bot.register_next_step_handler(msg, process_name_step)
        elif message.text.lower() == "главное меню":
            bot.send_message(message.chat.id, 'Перевожу!',
                             reply_markup=utils.generate_mainMenu_markup())
        else:
            time = datetime.datetime.strptime(message.text, '%H:%M')
            user = user_dict[chat_id]
            user.time = time
            msg = bot.reply_to(message, "Остался последний шаг, запишем номер телефона",
                               reply_markup=utils.generate_markup(["В начало", "Главное меню"]))
            bot.register_next_step_handler(msg, process_phone_step)
    except:
        msg = bot.send_message(message.chat.id, "Нажимай кнопку, а не пиши сам.")
        # генерирую клаву
        bot.register_next_step_handler(msg, process_time_step)


def process_phone_step(message):
    try:
        if message.text.lower() == "в начало":
            msg = bot.reply_to(message, "Хорошо, давай перезапишем Ваше имя.",
                               reply_markup=utils.generate_markup(["Главное меню"]))
            bot.register_next_step_handler(msg, process_name_step)
        elif message.text.lower() == "главное меню":
            bot.send_message(message.chat.id, 'Перевожу!',
                             reply_markup=utils.generate_mainMenu_markup())
        else:
            chat_id = message.chat.id
            user = user_dict[chat_id]
            if utils.check_phone(message.text):
                user.phone = message.text
                recorder.makeEntry(buttonTime=user.time.strftime('%H:%M'), dateButton=get_datetime_from_data(user.day),
                                   MFCButton=user.MFC, phoneNumber=user.phone,
                                   chatID=chat_id, name=user.name)

                bot.reply_to(message, f"Ты записан!\nИмя: {user.name}\nВремя: {user.time.strftime('%H:%M')}\n"
                                      f"День: {user.day}\nТелефон: {user.phone}", reply_markup=utils.generate_mainMenu_markup())
            else:
                msg = bot.reply_to(message, "Меня не проведешь, вводи настоящий номер!")
                bot.register_next_step_handler(msg, process_phone_step)
    except Exception as e:
        print(e)
        bot.reply_to(message, utils.error_message())
        bot.send_message(message.chat.id, 'Вернула!', reply_markup=utils.generate_mainMenu_markup())


bot.polling()
