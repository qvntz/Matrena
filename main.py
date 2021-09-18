from answererControl import AnswererControl

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
    # Получить главное меню словаря кнопок
    for button in control.getMainMenu().getChildrens():
        print(button.display())
