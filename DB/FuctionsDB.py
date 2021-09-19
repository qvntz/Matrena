from typing import List

from DB.MakeDB import MFC, Times, session
from DB.Tools import get_data_from_str
from arсhive.finder_mfc import haversine
# Получить id по имени
from exceptions.dataBaseException import DataBaseException


def getID(nameMFC: str) -> int:
    return session.query(MFC).filter(MFC.name == nameMFC).first().id


# Получить координаты по имени
def getCord(name: str):
    temp = session.query(MFC).filter(MFC.name == name).first()
    return temp.x, temp.y


# Получить массив всех доступных времен
def getDate(nameMFC: str) -> list:
    temp = session.query(Times).filter(
        Times.mfc_id == session.query(MFC).filter(MFC.name == nameMFC).first().id).filter(
        Times.chat_id == 'N').all()
    res = []
    for i in temp:
        res.append(i.date)

    return sorted(list(set(res)))


def getFreeTimes(nameMFC: str, date: str) -> list:
    id = getID(nameMFC)
    temp = session.query(Times).filter((Times.mfc_id == id), (Times.chat_id == 'N'), (Times.date == date)).all()
    res = []
    for i in temp:
        res.append(i.time)
    return res


# Получить все названия МФЦ
def getMFCsNames() -> list:
    temp = session.query(MFC).all()
    res = []
    for i in temp:
        res.append(i.name)
    return res


# Получить название ближайего
def getNearestMfc(x1: float, y1: float):
    temp = session.query(MFC).all()
    res = []
    temp1 = []
    temp2 = []
    for i in temp:
        temp1.append(i.name)
        temp2.append(haversine(i.x, i.y, x1, y1))
    res = temp1[temp2.index(min(temp2))]
    return res


# Записать человека по логину в телеграмме , имени , фамилии и номеру телефона
# def setRecord(date: str, time: str, nameMFC: str, chat_id: str, name: str, telephone: str):
#     try:
#         if time in getFreeTimes(nameMFC, date):
#             session.query(Times).filter((Times.mfc_id == session.query(MFC).filter(MFC.name == nameMFC).first().id),
#                                         (Times.time == time), (Times.date == date)).update({'chat_id': chat_id,
#                                                                                             'name': name,
#                                                                                             'telephone': telephone})
#             session.commit()
#             print('Done ', chat_id, ' - ', time)
#         else:
#             print('No this time ')
#     except Exception as e:
#         print(e)
def setRecord(date : str, time: str, nameMFC: str, chat_id: str, name: str, telephone: str):
    try:
        if str(time) in getFreeTimes(nameMFC , str(date)):
            session.query(Times).filter((Times.mfc_id == session.query(MFC).filter(MFC.name == nameMFC).first().id),
                                        (Times.time == time), (Times.date == date)).update({'chat_id': chat_id,
                                                                      'name': str(name),
                                                                      'telephone': str(telephone)})
            session.commit()
            print('Done ', chat_id, ' - ', time)
        else:
            print('No this time ')
    except Exception as e:
        print(e)

# 'surname': surname,   surname: str


# Получить данные о записи по имени
def getRecordByName(name: str) -> List[str]:
    try:
        temp = session.query(Times).filter((Times.name == name)).first()
        return [temp.time, get_data_from_str(str(temp.date)), session.query(MFC).filter(
            MFC.id == temp.mfc_id).first().name]

    except Exception as e:
        print(e)


# Получить данные о записи по логину
def getRecordByUsername(username: str) -> List[str]:
    try:
        temp = session.query(Times).filter(Times.chat_id == username).first()
        return [temp.time, get_data_from_str(str(temp.date)), session.query(MFC).filter(
            MFC.id == temp.mfc_id).first().name]

    except Exception as e:
        return []

'''Tests'''
# print('getCord')
# print(getCord('МФЦ Адмиралтейского района'))
# print('getID')
# print(getID('МФЦ Калининского района'))
# print('getMFCsNames')
# print(getMFCsNames())
# print('getFreeTimes')
# print(getFreeTimes('МФЦ Василеостровского района'))
# print('Add new record to mfc')
# setRecord('13.00', 'МФЦ Василеостровского района', 'Andrey_Varan', 'Andrey ', 'Perevoshikov ', '89098172313')
# print(getFreeTimes('МФЦ Василеостровского района'))
# print('getRecordByName')
# print(getRecordByName('Andrey ', 'Perevoshikov '))
# print('getRecordByUsername')
# print(getRecordByUsername('Andrey_Varan'))
