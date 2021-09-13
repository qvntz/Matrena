from Architecture.parseJson import parsedJson

if __name__ == '__main__':

    # Пример работы с прослойкой
    parsedJson1 = parsedJson()
    parsedJson1.parseJson()
    # Словарь с кнопками
    dict1 = parsedJson1.getButtonsDict()
    button = dict1.get("Паспорт")
    for i in button.getChildrens():
        print(i.display())
    # Меню в основе
    print()
    mainMenu = parsedJson1.getMainMenu()
    for i in mainMenu.getChildrens():
        print(i.display())
    # answerer = Answerer()
    # df = answerer.giveAnswer('Пособие')
    # print(df)
