from collections import OrderedDict
from typing import Dict, Optional

from pandas import DataFrame

from Architecture.element import Button, Answer, Element
from DB.FuctionsDB import *
from definitions import DF
from exceptions.dataBaseException import DataBaseException


class RecordControl:
    # Преобразование датафрейма в кнопку , дети которой - способы и тд
    @staticmethod
    def queryDfToButton(df: DataFrame) -> Button:
        questionButton = Button(df.iloc[0][DF.QUESTION.value])
        for index, row in df.iterrows():
            button = Button(row[DF.METHOD.value])
            button.addChild(Answer(text=row[DF.DOCS.value], question=DF.DOCS.value))
            button.addChild(Answer(text=row[DF.ACTIONS.value], question=DF.ACTIONS.value))
            button.addChild(Answer(text=row[DF.LINK.value], question=DF.LINK.value))
            questionButton.addChild(button)
        return questionButton

    @staticmethod
    def __listToButtonsDict(array: list) -> Dict[str, Button]:
        buttonsDict = OrderedDict()
        for item in array:
            newButton = Button(text=item)
            buttonsDict[item] = newButton
        return buttonsDict

    @staticmethod
    def makeEntry(MFCButton, dateButton, buttonTime, chatID: str, name: str,
                  phoneNumber: Optional[str] = None):
        phoneNumber = "-" if phoneNumber is None else phoneNumber
        try:
            setRecord(time=buttonTime, date=dateButton, nameMFC=MFCButton,
                      chat_id=chatID,
                      name=name, telephone=phoneNumber)
        except DataBaseException as e:
            print("Can not make entry with username " + chatID)

    def getMFCsDict(self) -> Dict[str, Button]:
        MFCs = getMFCsNames()
        return self.__listToButtonsDict(MFCs)

    def __getDictFreeTimesByButton(self, MFCButton: Button, dateButton: Button) -> Dict[str, Button]:
        freeTimesList = getFreeTimes(date=dateButton.display(), nameMFC=MFCButton.display())
        freeTimesButtons = self.__listToButtonsDict(freeTimesList)
        for freeTime in freeTimesButtons.values():
            dateButton.addChild(freeTime)
        return freeTimesButtons

    def initializeFreeDates(self, MFCButton: Button):
        freeDatesList = getDate(MFCButton.display())
        freeDatesButtons = self.__listToButtonsDict(freeDatesList)
        # add Dates to MFC button
        for freeDate in freeDatesButtons.values():
            MFCButton.addChild(freeDate)
            # add Times buttons to Date button
            freeTimes = self.__getDictFreeTimesByButton(MFCButton=MFCButton, dateButton=freeDate)

    @staticmethod
    def getInfoByName(name: str) -> List[str]:
        timeNameList = getRecordByName(name=name)
        return timeNameList

    @staticmethod
    def getInfoAboutRecordByChatID(chatID: str) -> List[str]:
        timeNameList = getRecordByUsername(chatID)
        return timeNameList

    @staticmethod
    def getNearestMFCButton(x: float, y: float) -> Button:
        return Button(text=getNearestMfc(x, y))
