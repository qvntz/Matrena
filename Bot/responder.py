from answererControl import AnswererControl
from Bot.utils import generate_markup
import time


# --------------- Сценарий ответа на вопрос ---------------
# --------------- Сценарий ответа на вопрос ---------------


def get_answer(message, bot):
    control = AnswererControl()
    print(control)
    dict1 = control.answerForQuery(message.text)
    print(dict1.keys())
    msg = bot.send_message(message.chat.id, "Уже ищу..!\n",
                           reply_markup=generate_markup(dict1.keys(), width=1))
    bot.register_next_step_handler(msg, lambda m: choise_method_step(m, bot, dict1))


def choise_method_step(message, bot, dict1):
    a = []
    if message.text + " " in dict1:
        for i in dict1[message.text + " "].getChildrens():
            a.append(i.display())

        msg = bot.send_message(message.chat.id, "Я прикрепил снизу все ссылки, чтобы тебе было удобнее.",
                               reply_markup=generate_markup(a, width=2))
        bot.register_next_step_handler(msg, lambda m: choise_step(m, bot, dict1[message.text + " "]))
    else:
        msg = bot.send_message(message.chat.id, "Я прикрепил снизу все ссылки, чтобы тебе было удобнее.",
                               reply_markup=generate_markup(a, width=2))
        bot.reply_to(message, "Упс(")


def choise_step(message, bot, list1):
    a = []
    temp = []
    for i in list1.getChildrens():
        if i.display() == message.text:
            for j in i.getChildrens():
                temp.append(j)
                a.append(j.display())
            break
    msg = bot.send_message(message.chat.id, "Я прикрепил снизу все ссылки, чтобы тебе было удобнее.",
                           reply_markup=generate_markup(a, width=5))
    bot.register_next_step_handler(msg, lambda m: choise_interest_step(m, bot, temp))


def choise_interest_step(message, bot, list1):
    for i in list1:
        if message.text == i.display():
            msg = i.getMessage().splitlines()
            for i in msg:
                bot.send_message(message.chat.id, i)
                time.sleep(0.1)
            break
