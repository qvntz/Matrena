import json
from typing import Optional

from element import Answer, Button


def parseJson(jsonPath: Optional[str] = 'data/answers.json'):
    buttonsDict = {}
    buttons = []
    texts = {}
    with open(jsonPath, encoding="utf-8") as json_data:
        data = json.loads(json_data.read())
        for component in data["QAs"]:

            # create QA dict
            if component["type"] == "text":
                answers = ""
                for answer in component["answers"]:
                    answers += answer
                    answers += '\n'
                newQA = Answer(answers)
                texts[component["question"].lower()] = newQA

            # Create buttons dict
            if component["type"] == "button":
                buttonsDict[component["question"]] = Button(component["question"], childrens=[],
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
        #                 available_times = get_free_times(current_mfc)
        #                 messageForUser = "Доступное время для записи в " + current_mfc
        #                 newButton = element("button", available_times, messageForUser)
        #                 self.elements[current_mfc.lower()] = newButton
        #                 # Add time's buttons
        #                 for iTime in available_times:
        #                     newTimeButton = element("time")
        #                     self.elements[iTime] = newTimeButton
        for button in buttonsDict.values():
            for child in button.getPotentialChilds():
                if child in buttonsDict.keys():
                    button.addChild(buttonsDict[child])
                if child in texts.keys():
                    button.addChild(texts[child])
    return buttonsDict


if __name__ == '__main__':
    dict1 = parseJson()
    a = dict1.get("СНИЛС")
    for i in a.getChildrens():
        print(i.display())
