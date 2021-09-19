from typing import Dict

from pandas import DataFrame

from Answerer.answerer import Answerer
from Architecture.element import *
from Architecture.parseJson import parsedJson
from definitions import JSON_BUTTONS_FILE
from recordControl import RecordControl


class AnswererControl:
    __dataPath = JSON_BUTTONS_FILE

    def __init__(self):
        self.__data = parsedJson(self.__dataPath)
        self.__data.parseJson()
        self.__answerer = Answerer()

    def getButtonsDict(self):
        return self.__data.getButtonsDict()

    # Получить главное меню словаря кнопок
    def getMainMenu(self) -> Button:
        return self.__data.getMainMenu()

    def __giveAnswer(self, question: str) -> List[DataFrame]:
        try:
            return self.__answerer.giveAnswer(question)[:3]
        except TypeError as e:
            print("Answerer problems: ", e)

    # Работа с запросом пользователя
    # Пока что один овтет , но должно быть 3 , которые будут полученые от Answerer и добавлены в словарь AnswerDict
    def answerForQuery(self, query: str) -> Dict[str, Button]:
        answersDict = {}
        answersDf = self.__giveAnswer(query)
        if not answersDf:
            return answersDict
        for dfAnswer in answersDf:
            button = RecordControl.queryDfToButton(dfAnswer)
            # Тут всплыла проблема : добавление поля вопроса в класс Button , если нам предстоит менять текст
            # после тыка по кнопке с нужным вопросом из трех предложенных нейронкой , то надо его добавлять и меня метод
            # queryDfToButton
            answersDict[button.display()] = button
        return answersDict