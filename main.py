from answererControl import AnswererControl
from recordControl import RecordControl

if __name__ == '__main__':
    control = AnswererControl()

    # Запрос пользователя
    # dict1 = control.answerForQuery('Замена паспорт')

    # Словарь содержит кнопки с ответами, дети кнопок элементы таблицы со следующей иерархией:
    # Вопрос -> Способ -> Документы, Порядок действий , Ссылка
    # for key in dict1:
    #     print(key)
    #     for method in dict1[key].getChildrens():
    #         print(method.display())
    #         for info in method.getChildrens():
    #             print(info.display(), end=' ')
    #             # тут весь текст
    #             # print(info.getText())
    #             print()
    #     print()
    # # # Получить главное меню словаря кнопок
    # for element in control.getMainMenu().getChildrens():
    #     print(element.display())

    ### Тест записи

    # Создание заглушки бд мфц
    # Base.metadata.create_all(bind=engine)
    # post_MFC()

    recorder = RecordControl()
    # Format for time hh:mm
    MFCs = recorder.getMFCsDict()
    for MFCName in MFCs:
        MFCButton1 = MFCs.get(MFCName)
        freeDatesDict = recorder.displayFreeDatesByButton(MFCs.get(MFCName))
        for dateButton in freeDatesDict.values():
            for timeButton in dateButton.getChildrens():
                recorder.makeEntry(buttonTime=timeButton, dateButton=dateButton, MFCButton=MFCs.get(MFCName),
                                   name="Илья", surname="Шевчук",
                                   username="ilyaShevchuk77")
                break
            break
        break
    print(recorder.getInfoAboutRecordByName("Илья", "Шевчук"))
