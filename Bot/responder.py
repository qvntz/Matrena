from answererControl import AnswererControl
from Bot.utils import generate_markup


def get_answer(message, bot):
    control = AnswererControl()
    print(message.text)
    dict1 = control.answerForQuery(message.text)
    print(dict1.keys())
    bot.send_message(message.chat.id, "Я прикрепил снизу все ссылки, чтобы тебе было удобнее.",
                     reply_markup=generate_markup(dict1.keys()))