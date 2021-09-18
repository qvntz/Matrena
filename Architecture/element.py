from abc import abstractmethod, ABCMeta
from typing import List, Optional


class Element:
    __metaclass__ = ABCMeta

    # Возвращает надпись на кнопке
    @abstractmethod
    def display(self):
        raise NotImplementedError

    # Возвращает наслдеников
    @abstractmethod
    def getChildrens(self):
        raise NotImplementedError()

    # Возваращет текст выводимый пользователю (большой в случае Answer и маленький в случае Button)
    @abstractmethod
    def getMessage(self):
        raise NotImplementedError


class Button(Element):

    def getMessage(self):
        return self.__message

    def display(self) -> str:
        return self.__message

    def getChildrens(self) -> List[Element]:
        return self.__childrens

    def __init__(self, text: str, childrens: Optional[List[Element]] = None,
                 potentialChilds: Optional[List[str]] = None):
        self.__message = text
        self.__childrens = [] if childrens is None else childrens
        self.__potentialChilds = [] if potentialChilds is None else potentialChilds

    def addChild(self, element: Element):
        self.__childrens.append(element)

    def getPotentialChilds(self):
        return self.__potentialChilds


class Answer(Element):
    def display(self):
        return self.__question

    __message = "Not implemented Answer.__text"
    __question = "Not implemented Answer.__question"

    def __init__(self, text: str, question: Optional[str] = ""):
        self.__message = text
        self.__question = question

    # Возвращает answers
    def getMessage(self):
        # Возможно этому место в getChildrens(self)
        return self.__message

    def getChildrens(self) -> list:
        return list()
