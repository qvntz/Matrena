import json
from typing import Optional

from Architecture.element import Answer, Button
from definitions import JSON_BUTTONS_FILE


class parsedJson:
    def __init__(self, jsonPath: Optional[str] = JSON_BUTTONS_FILE):
        self.__buttonsDict = {}
        self.__texts = {}
        self.jsonPath = jsonPath

    def parseJson(self):
        with open(self.jsonPath, encoding="utf-8") as json_data:
            data = json.loads(json_data.read())
            for component in data["QAs"]:

                # create QA dict
                if component["type"] == "text":
                    answers = ""
                    for answer in component["answers"]:
                        answers += answer
                        answers += '\n'
                    newQA = Answer(question=component["question"], text=answers)
                    self.__texts[component["question"]] = newQA

                # Create buttons dict
                if component["type"] == "button":
                    self.__buttonsDict[component["question"]] = Button(component["question"], childrens=[],
                                                                       potentialChilds=component["buttons"])
                    # newButton = Button(text=component["message"], childrens=buttonsChilds)
                    # newButtonsList = element("button", buttons, component["message"])
                    # self.elements[component["question"].lower()] = newButtonsList

            #         if component["occupancy"]:
            #             MFCs = get_names()
            #             newMFCList = element("button", component["buttons"] + MFCs, component["message"])
            #             self.elements[component["question"].lower()] = newMFCList
            #             # add button for MFCs
            #             for current_mfc in MFCs:
            #                 available_times = getFreeTimes(current_mfc)
            #                 messageForUser = "Доступное время для записи в " + current_mfc
            #                 newButton = element("button", available_times, messageForUser)
            #                 self.elements[current_mfc.lower()] = newButton
            #                 # Add time's buttons
            #                 for iTime in available_times:
            #                     newTimeButton = element("time")
            #                     self.elements[iTime] = newTimeButton

            self.__generateButtonDict()

    def __generateButtonDict(self):
        for button in self.__buttonsDict.values():
            for child in button.getPotentialChilds():
                if child in self.__buttonsDict.keys():
                    button.addChild(self.__buttonsDict[child])
                if child in self.__texts.keys():
                    button.addChild(self.__texts[child])

    def getButtonsDict(self):
        return self.__buttonsDict

    def getMainMenu(self)-> Button:
        mainMenuInJson = "Главное меню"
        return self.getButtonsDict().get(mainMenuInJson)
