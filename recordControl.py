from typing import Dict, Optional, Tuple

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
        buttonsDict = {}
        for item in array:
            newButton = Button(text=item)
            buttonsDict[item] = newButton
        return buttonsDict

    @staticmethod
    def makeEntry(MFCButton: Button, dateButton: Button, buttonTime: Element, username: str, name: str,
                  surname: str, phoneNumber: Optional[str] = None):
        phoneNumber = "-" if phoneNumber is None else phoneNumber
        try:
            setRecord(time=buttonTime.display(), date=dateButton.display(), nameMFC=MFCButton.display(),
                      username=username,
                      name=name, surname=surname, telephone=phoneNumber)
        except DataBaseException as e:
            print("Can not make entry with username " + username)

    def getMFCsDict(self) -> Dict[str, Button]:
        MFCs = getMFCsNames()
        return self.__listToButtonsDict(MFCs)

    def displayFreeTimesByButton(self, MFCButton: Button, dateButton: Button) -> Dict[str, Button]:
        freeTimesList = getFreeTimes(date=dateButton.display(), nameMFC=MFCButton.display())
        freeTimesButtons = self.__listToButtonsDict(freeTimesList)
        for freeTime in freeTimesButtons.values():
            dateButton.addChild(freeTime)
        return freeTimesButtons

    def displayFreeDatesByButton(self, MFCButton: Button) -> Dict[str, Button]:
        freeDatesList = getDate(MFCButton.display())
        freeDatesButtons = self.__listToButtonsDict(freeDatesList)
        # add Dates to MFC button
        for freeDate in freeDatesButtons.values():
            MFCButton.addChild(freeDate)
            # add Times buttons to Date button
            freeTimes = self.displayFreeTimesByButton(MFCButton=MFCButton, dateButton=freeDate)
            for freeTimeButton in freeTimes.values():
                freeDate.addChild(freeTimeButton)
        return freeDatesButtons

    @staticmethod
    def getInfoAboutRecordByName(name: str, surname: str) -> Tuple[str, str]:
        timeNameTuple = getRecordByName(name=name, surname=surname)
        return timeNameTuple

    @staticmethod
    def getInfoAboutRecordByUsername(username: str) -> Tuple[str, str]:
        timeNameTuple = getRecordByUsername(username)
        return timeNameTuple

    @staticmethod
    def getNearestMFCButton(x: float, y: float) -> Button:
        return Button(text=getNearestMfc(x, y))
