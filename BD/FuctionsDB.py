from archive.finder_mfc import haversine
from MakeDB import MFC, Times, session


# Получить id по имени
def get_id(nameMFC: str) -> int:
    return session.query(MFC).filter(MFC.name == nameMFC).first().id


# Получить координаты по имени
def get_cord(namen: str):
    temp = session.query(MFC).filter(MFC.name == namen).first()
    return temp.x, temp.y


# Получить массив всех доступных времен
def get_free_times(nameMFC: str):
    temp = session.query(Times).filter(
        Times.mfc_id == session.query(MFC).filter(MFC.name == nameMFC).first().id).filter(
        Times.username == 'N').all()
    res = []
    for i in temp:
        res.append(i.time)
    res = sorted(res)
    return res


# Получить все названия МФЦ
def get_all_names():
    temp = session.query(MFC).all()
    res = []
    for i in temp:
        res.append(i.name)
    return res


# Получить название ближайего
def get_neerest_mfc(x1: float, y1: float):
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
def set_record(time: str, nameMFC: str, username: str, name: str, surname: str, telephone: str):
    try:
        if time in get_free_times(nameMFC):
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
def get_record_by_name(name: str, surname: str):
    try:
        temp = session.query(Times).filter((Times.name == name), (Times.surname == surname)).first()
        return temp.time, session.query(MFC).filter(MFC.id == temp.id).first().name

    except Exception as e:
        print(e)


# Получить данные о записи по логину
def get_record_by_username(username: str):
    try:
        temp = session.query(Times).filter(Times.username == username).first()
        return temp.time, session.query(MFC).filter(MFC.id == temp.id).first().name

    except Exception as e:
        print(e)


'''Tests'''
# print('get_cord')
# print(get_cord('МФЦ Адмиралтейского района'))
# print('get_id')
# print(get_id('МФЦ Калининского района'))
# print('get_all_names')
# print(get_all_names())
# print('get_free_times')
# print(get_free_times('МФЦ Василеостровского района'))
# print('Add new record to mfc')
# set_record('13.00', 'МФЦ Василеостровского района', 'Andrey_Varan', 'Andrey ', 'Perevoshikov ', '89098172313')
# print(get_free_times('МФЦ Василеостровского района'))
# print('get_record_by_name')
# print(get_record_by_name('Andrey ', 'Perevoshikov '))
# print('get_record_by_username')
# print(get_record_by_username('Andrey_Varan'))
