from arсhive.finder_mfc import haversine
from DB.MakeDB import MFC, Times, session


# Получить id по имени
from exceptions.dataBaseException import DataBaseException


def getID(nameMFC: str) -> int:
    return session.query(MFC).filter(MFC.name == nameMFC).first().id


# Получить координаты по имени
def getCord(name: str):
    temp = session.query(MFC).filter(MFC.name == name).first()
    return temp.x, temp.y


# Получить массив всех доступных времен
def getFreeTimes(nameMFC: str) -> list:
    temp = session.query(Times).filter(
        Times.mfc_id == session.query(MFC).filter(MFC.name == nameMFC).first().id).filter(
        Times.username == 'N').all()
    res = []
    for i in temp:
        res.append(i.time)
    res = sorted(res)
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
def setRecord(time: str, nameMFC: str, username: str, name: str, surname: str, telephone: str):
    try:
        if time in getFreeTimes(nameMFC):
            session.query(Times).filter((Times.mfc_id == session.query(MFC).filter(MFC.name == nameMFC).first().id),
                                        (Times.time == time)).update({'username': username,
                                                                      'name': name,
                                                                      'surname': surname,
                                                                      'telephone': telephone})
            session.commit()
            print('Done ', username, ' - ', time)
        else:
            print('No this time ')
    except Exception as e:
        print(e)


# Получить данные о записи по имени и фамилии
def getRecordByName(name: str, surname: str):
    try:
        temp = session.query(Times).filter((Times.name == name), (Times.surname == surname)).first()
        return temp.time, session.query(MFC).filter(MFC.id == temp.id).first().name

    except Exception as e:
        print(e)


# Получить данные о записи по логину
def getRecordByUsername(username: str):
    try:
        temp = session.query(Times).filter(Times.username == username).first()
        return temp.time, session.query(MFC).filter(MFC.id == temp.id).first().name

    except Exception as e:
        raise DataBaseException()


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
