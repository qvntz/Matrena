from pyaspeller import YandexSpeller

speller = YandexSpeller()


def spellCheck(phrase: str) -> str:
    return speller.spelled(phrase)
