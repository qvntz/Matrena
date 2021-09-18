# from answererControl import AnswererControl
from DB.MakeDB import add_MFC,delete_DB, Base , engine , post_MFC
from DB.UpdateDB import put_new_timeses, delete_past_time
from DB.FuctionsDB import *

if __name__ == '__main__':
    delete_DB()
    # control = AnswererControl()
    # Создание заглушки бд мфц
    Base.metadata.create_all(bind=engine)
    post_MFC()
    put_new_timeses(['МФЦ Адмиралтейского района', 'МФЦ Василеостровского района'], '2021-09-17')
    put_new_timeses(['МФЦ Адмиралтейского района', 'МФЦ Василеостровского района'], '2021-09-19')
    delete_past_time(['МФЦ Адмиралтейского района', 'МФЦ Василеостровского района'])
    datas = getDate('МФЦ Адмиралтейского района')
    print(datas)
    timese = getFreeTimes('МФЦ Адмиралтейского района',datas[0])
    print(timese)
    setRecord(datas[0] , timese[0], 'МФЦ Адмиралтейского района' ,'Andrey_Varan', 'Andrey ', 'Perevoshikov ', '89098172313' )
    print('getRecordByName')
    print(getRecordByName('Andrey ', 'Perevoshikov '))
    print('getRecordByUsername')
    print(getRecordByUsername('Andrey_Varan'))
    # print('Add new record to mfc')
    # setRecord('13.00', 'МФЦ Василеостровского района', 'Andrey_Varan', 'Andrey ', 'Perevoshikov ', '89098172313')
    # print(getFreeTimes('МФЦ Василеостровского района'))
    # print('getRecordByName')
    # print(getRecordByName('Andrey ', 'Perevoshikov '))
    # print('getRecordByUsername')
    # print(getRecordByUsername('Andrey_Varan'))
    # Удаление базы данных
    # delete_DB()

    # Запрос пользователя
    # dict1 = control.answerForQuery('Замена паспорт')
    # # Словарь содержит кнопки с ответами, дети кнопок элементы таблицы со следующей иерархией:
    # # Вопрос -> Способ -> Документы, Порядок действий , Ссылка
    # for key in dict1:
    #     print(key)
    #     for method in dict1[key].getChildrens():
    #         print(method.display())
    #         for info in method.getChildrens():
    #             print(info.display(), end=' ')
    #             # тут весь текст
    #             # print(info.getText())
    #         print()
    # print()
    # # Получить главное меню словаря кнопок
    # for button in control.getMainMenu().getChildrens():
    #     print(button.display())
