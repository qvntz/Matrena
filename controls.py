from typing import Dict

from pandas import DataFrame

from Answerer.answerer import Answerer
from Architecture.element import *
from Architecture.parseJson import parsedJson
from DB.FuctionsDB import *
from definitions import JSON_BUTTONS_FILE, DF


class Controls:
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

    def __giveAnswer(self, question: str) -> DataFrame:
        try:
            return self.__answerer.giveAnswer(question)
        except TypeError:
            print("Answerer problems")

    # Работа с запросом пользователя
    # Пока что один овтет , но должно быть 3 , которые будут полученые от Answerer и добавлены в словарь AnswerDict
    def answerForQuery(self, query: str) -> Dict[str, Button]:
        answersDict = {}
        answerDf = self.__giveAnswer(query)
        button = self.__QueryDfToButton(answerDf)
        # Тут всплыла проблема : добавление поля вопроса в класс Button , если нам предстоит менять текст
        # после тыка по кнопке с нужным вопросом из трех предложенных нейронкой , то надо его добавлять и меня метод
        # __QueryDfToButton
        answersDict[button.display()] = button
        return answersDict

    # Преобразование датафрейма в кнопку , дети которой - способы и тд
    @staticmethod
    def __QueryDfToButton(df: DataFrame) -> Button:
        questionButton = Button(df.iloc[0][DF.QUESTION.value])
        for index, row in df.iterrows():
            button = Button(row[DF.METHOD.value])
            button.addChild(Answer(text=row[DF.DOCS.value], question=DF.DOCS.value))
            button.addChild(Answer(text=row[DF.ACTIONS.value], question=DF.ACTIONS.value))
            button.addChild(Answer(text=row[DF.LINK.value], question=DF.LINK.value))
            questionButton.addChild(button)
        return questionButton

    @staticmethod
    def __listToButtonsDict(array: list) -> Dict[Button]:
        buttonsDict = {}
        for item in array:
            newButton = Button(text=item)
            buttonsDict[item] = newButton
        return buttonsDict

    def displayMFCs(self) -> Dict[Button]:
        MFCs = getMFCsNames()
        return self.__listToButtonsDict(MFCs)

    def displayEntryOptionsByButton(self, MFCButton: Button) -> Dict[Button]:
        freeTimesList = get_free_times(MFCButton.display())
        freeTimesButtons = self.__listToButtonsDict(freeTimesList)
        for freeTime in freeTimesButtons:
            MFCButton.addChild(freeTime)
        return freeTimesButtons

    def makeEntry(self, buttonTime: Button, MFCButton: Button, username: str, name: str,
                  surname: str, phoneNumber: Optional[str] = None):
        phoneNumber = "-" if phoneNumber is None else phoneNumber
        try:
            set_record(time=buttonTime.display(), nameMFC=MFCButton.display(), username=username,
                       name=name, surname=surname, telephone=phoneNumber)
        except DataBaseException as e:
            print()

    def nearestMFC(self):
        pass
        # todo Поиск ближайшего МФЦ
