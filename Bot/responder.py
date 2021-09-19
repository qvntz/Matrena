from answererControl import AnswererControl
from Bot.utils import generate_markup
import time

def get_answer(message, bot):
    control = AnswererControl()
    dict1 = control.answerForQuery(message.text)
    msg = bot.send_message(message.chat.id, "Я прикрепил снизу все ссылки, чтобы тебе было удобнее.",
                           reply_markup=generate_markup(dict1.keys()))
    bot.register_next_step_handler(msg, lambda m: choise_method_step(m, bot, dict1))


def choise_method_step(message, bot, dict1):
    a = []
    for i in dict1[message.text + " "].getChildrens():
        a.append(i.display())

    msg = bot.send_message(message.chat.id, "Я прикрепил снизу все ссылки, чтобы тебе было удобнее.",
                           reply_markup=generate_markup(a))
    bot.register_next_step_handler(msg, lambda m: choise_step(m, bot, dict1[message.text + " "]))


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
                           reply_markup=generate_markup(a))
    bot.register_next_step_handler(msg, lambda m: choise_interest_step(m, bot, temp))


def choise_interest_step(message, bot, list1):
    for i in list1:
        if message.text == i.display():
            msg = i.getMessage().splitlines()
            for i in msg:
                bot.send_message(message.chat.id, i)
                time.sleep(0.1)
            break