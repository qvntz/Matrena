from answererControl import AnswererControl
from recordControl import RecordControl

if __name__ == '__main__':
    control = AnswererControl()

    # Запрос пользователя
    dict1 = control.answerForQuery('Замена паспорт')

    # Словарь содержит кнопки с ответами, дети кнопок элементы таблицы со следующей иерархией:
    # Вопрос -> Способ -> Документы, Порядок действий , Ссылка
    for key in dict1:
        print(key)
        for method in dict1[key].getChildrens():
            print(method.display())
            for info in method.getChildrens():
                print(info.display(), end=' ')
                # тут весь текст
                # print(info.getText())
                print()
        print()
    # # Получить главное меню словаря кнопок
    for element in control.getMainMenu().getChildrens():
        print(element.display())

    ### Тест записи

    # Создание заглушки бд мфц
    # Base.metadata.create_all(bind=engine)
    # add_MFC()

    recorder = RecordControl()
    # Format for time hh:mm
    countForGetOnlyFirstInDict = 0
    buttonTime1 = 0
    MFCButton1 = 0
    MFCs = recorder.getMFCsDict()
    for MFCName in MFCs:
        MFCButton1 = MFCs.get(MFCName)
        freeTimesDict = recorder.displayEntryOptionsByButton(MFCs.get(MFCName))
        for timeButton in freeTimesDict.values():
            buttonTime1 = timeButton
            recorder.makeEntry(buttonTime=timeButton, MFCButton=MFCs.get(MFCName), name="Илья", surname="Шевчук",
                               username="ilyaShevchuk77")
            break
        break
    print(recorder.getInfoAboutRecordByName("Илья", "Шевчук"))
