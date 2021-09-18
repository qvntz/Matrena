from DB.MakeDB import delete_DB, Base, engine, post_MFC
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
                print()
                '''print(info.getMessage())
                # тут весь текст
                # print(info.getText())
                print()'''
        print()
