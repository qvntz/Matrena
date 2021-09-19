from answererControl import AnswererControl
from Bot.utils import generate_markup, generate_mainMenu_markup
import time


# --------------- Сценарий ответа на вопрос ---------------
# --------------- Сценарий ответа на вопрос ---------------


def get_answer(message, bot):
    control = AnswererControl()
    dict1 = control.answerForQuery(message.text)
    if dict1:
        msg = bot.send_message(message.chat.id, "Уже ищу..!\n",
                               reply_markup=generate_markup(dict1.keys(), width=1))
        bot.register_next_step_handler(msg, lambda m: choise_method_step(m, bot, dict1))
    else:
        bot.send_message(message.chat.id, "Я еще такого не знаю, давайте попробуем еще раз!",
                         reply_markup=generate_mainMenu_markup())


def choise_method_step(message, bot, dict1):
    a = []
    if message.text + " " in dict1:
        for i in dict1[message.text + " "].getChildrens():
            a.append(i.display())

        msg = bot.send_message(message.chat.id, "Где Вы хотите получить услугу?",
                               reply_markup=generate_markup(a, width=2))
        bot.register_next_step_handler(msg, lambda m: choise_step(m, bot, dict1[message.text + " "]))
    else:
        bot.send_message(message.chat.id, "Вижу, что мои варианты Вам не понравились, перевожу в главное меню",
                         reply_markup=generate_mainMenu_markup())


def choise_step(message, bot, list1):
    if message.text.lower() not in ("онлайн", "мфц", "офлайн"):
        bot.send_message(message.chat.id, "Так оказывать услугу я еще не умею!",
                         reply_markup=generate_mainMenu_markup())
    else:
        a = []
        temp = []
        for i in list1.getChildrens():
            if i.display() == message.text:
                for j in i.getChildrens():
                    temp.append(j)
                    a.append(j.display())
                break
        msg = bot.send_message(message.chat.id, "Что Вас интересует?",
                               reply_markup=generate_markup(a, width=5))
        bot.register_next_step_handler(msg, lambda m: choise_interest_step(m, bot, temp))


def choise_interest_step(message, bot, list1):
    if message.text.lower() not in ("ссылка", "документы", "порядок действий"):
        bot.send_message(message.chat.id, "Скоро изучу и этот аспект, а пока я так не могу(",
                         reply_markup=generate_mainMenu_markup())
    else:
        for i in list1:
            if message.text == i.display():
                msg = i.getMessage().splitlines()
                for i in msg:
                    if not i: continue
                    bot.send_message(message.chat.id, i)
                    time.sleep(0.2)
                break
