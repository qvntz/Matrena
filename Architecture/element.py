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
    _text = "Not implemented Button.__text"
    __potentialChilds = []
    __childrens = []

    def __init__(self, text: str, childrens: Optional[List[Element]], potentialChilds: Optional[List[str]]):
        self.__childrens = childrens
        self._text = text
        self.__potentialChilds = potentialChilds

    # Возвращает message
    def display(self) -> str:
        return self._text

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
