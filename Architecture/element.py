from abc import abstractmethod, ABCMeta
from typing import List, Optional


class Element:
    __metaclass__ = ABCMeta

    @abstractmethod
    def display(self):
        return NotImplementedError()

    @abstractmethod
    def getChildrens(self):
        return NotImplementedError()


class Button(Element):
    __text = "Not implemented Button.__text"

    def __init__(self, text: str, childrens: Optional[List[Element]] = None, potentialChilds: Optional[List[str]] = None):
        self.__text = text
        self.__childrens = [] if childrens is None else childrens
        self.__potentialChilds = [] if potentialChilds is None else potentialChilds

    # Возвращает message
    def display(self) -> str:
        return self.__text

    def addChild(self, element: Element):
        self.__childrens.append(element)

    # Возвращает всех наследников
    def getChildrens(self) -> List[Element]:
        return self.__childrens

    def getPotentialChilds(self):
        return self.__potentialChilds


class Answer(Element):
    __text = "Not implemented Answer.__text"
    __question = "Not implemented Answer.__question"

    def __init__(self, question: str, text: str):
        self.__text = text
        self.__question = question

    # Возвращает question
    def display(self) -> str:
        return self.__question

    # Возвращает answers
    def getText(self):
        # Возможно этому место в getChildrens(self)
        return self.__text

    def getChildrens(self):
        # todo
        return None
