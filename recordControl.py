from typing import Dict, Optional

from pandas import DataFrame

from Architecture.element import Button, Answer
from DB.FuctionsDB import getMFCsNames, getFreeTimes, setRecord, getRecordByName, getRecordByUsername
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
    def makeEntry(buttonTime: Button, MFCButton: Button, username: str, name: str,
                  surname: str, phoneNumber: Optional[str] = None):
        phoneNumber = "-" if phoneNumber is None else phoneNumber
        try:
            setRecord(time=buttonTime.display(), nameMFC=MFCButton.display(), username=username,
                      name=name, surname=surname, telephone=phoneNumber)
        except DataBaseException as e:
            print("Can not make entry with username " + username)

    def displayMFCs(self) -> Dict[str, Button]:
        MFCs = getMFCsNames()
        return self.__listToButtonsDict(MFCs)

    def displayEntryOptionsByButton(self, MFCButton: Button) -> Dict[str, Button]:
        freeTimesList = getFreeTimes(MFCButton.display())
        freeTimesButtons = self.__listToButtonsDict(freeTimesList)
        for freeTime in freeTimesButtons.values():
            MFCButton.addChild(freeTime)
        return freeTimesButtons

    def getInfoAboutRecordOptional(self, name: Optional[str] = None, username: Optional[str] = None):
        if name is not None:
            x = getRecordByName(name)
            # todo prepare x
            return x
        if username is not None:
            x = getRecordByUsername(username)
            # todo prepare x
            return x

    def getNearestMFC(self):
        # todo
        pass
