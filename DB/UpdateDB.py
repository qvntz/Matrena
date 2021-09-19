from datetime import datetime
from typing import List

from DB.FuctionsDB import getID
from DB.MakeDB import session, Times
from DB.Tools import get_list_times
from exceptions.dataBaseException import DataBaseException

names_MFC = ['МФЦ Адмиралтейского района', 'МФЦ Василеостровского района', 'МФЦ Выборгского района',
             'МФЦ Калининского района', 'МФЦ Кировского района', 'МФЦ Колпинского района',
             'МФЦ Красногвардейского района', 'МФЦ Красносельского района', 'МФЦ Кронштадтского района',
             'МФЦ Курортного района', 'МФЦ Московского района', 'МФЦ Невского района', 'МФЦ Петроградского района',
             'МФЦ Петродворцового района', 'МФЦ Приморского района', 'МФЦ Пушкинского района',
             'МФЦ Фрунзенского района']


def put_new_timeses(names_MFC: List[str], date: str):
    try:
        list_times = []
        for name in names_MFC:
            id = getID(name)
            for j in get_list_times(12):
                list_times.append(Times(time=j, date=date, mfc_id=id))
        session.add_all(list_times)
        session.commit()
    except Exception as e:
        raise DataBaseException()


format = '%Y-%m-%d'


def delete_past_time(names_mfc: List[str]):
    try:
        now = str(datetime.now().date())
        for name in names_MFC:
            id = getID(name)
            session.query(Times).filter((Times.mfc_id == id), (Times.date < now)).delete()
            session.commit()
    except Exception as e:
        pass
    #  ни в коем случае не меня на райз , хз почему но оно выводит ошибку , но рабоатет правильно


def delete_past_time_by_name(name_mfc):
    try:
        now = datetime.now()
        time = now.time()
        date = now.date()
        id = getID(name_mfc)
        session.query(Times).filter((Times.mfc_id == id), (Times.date <= str(date)) , (Times.time < str(time)[0:5])).delete()
        session.commit()
    except Exception as e:
        print(e)