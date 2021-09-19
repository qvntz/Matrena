from datetime import datetime, timedelta
from random import *
from typing import List


# Funcs
# -----------------------------------------------------------------------------------------------------------------------
def get_list_times(size: int):
    tuple_hourse = ('10', '11', '12', '13', '15', '16', '17')
    tuple_min = ('00', '10', '20', '30', '40', '50')
    result = []
    for i in range(size):
        temp_str = choice(tuple_hourse) + ':' + choice(tuple_min)
        result.append(temp_str)
    result = list(set(result))
    while len(result) < size:
        temp_str = choice(tuple_hourse) + ':' + choice(tuple_min)
        result.append(temp_str)
        result = sorted(list(set(result)))
    return sorted(list(set(result)))


def get_list_times_nrand():
    tuple_hourse = ('10', '11', '12', '13', '15', '16', '17')
    result = []
    for i in tuple_hourse:
        result.append(i + ':00')
        result.append(i + ':30')
    return result


def get_3_date() -> List[str]:
    temp_date = datetime.today().date()
    result = []
    result.append(str(temp_date))
    temp_date += timedelta(days=1)
    result.append(str(temp_date))
    temp_date += timedelta(days=1)
    result.append(str(temp_date))

    return result


# print(get_3_date())


def get_date_now():
    temp_date = datetime.today().date()
    return str(temp_date)


format = '%Y-%m-%d'


def get_datetime_from_data(date: str):
    temp_date = datetime.today().date().year
    if ' января' in date:
        return datetime(year=temp_date, day=int(date[0:2]), month=1).date()
    elif ' февраля' in date:
        return datetime(year=temp_date, day=int(date[0:2]), month=2).date()
    elif ' марта' in date:
        return datetime(year=temp_date, day=int(date[0:2]), month=3).date()
    elif ' апреля' in date:
        return datetime(year=temp_date, day=int(date[0:2]), month=4).date()
    elif ' мая' in date:
        return datetime(year=temp_date, day=int(date[0:2]), month=5).date()
    elif ' июня' in date:
        return datetime(year=temp_date, day=int(date[0:2]), month=6).date()
    elif ' июля' in date:
        return datetime(year=temp_date, day=int(date[0:2]), month=7).date()
    elif ' августа' in date:
        return datetime(year=temp_date, day=int(date[0:2]), month=8).date()
    elif ' сентября' in date:
        return datetime(year=temp_date, day=int(date[0:2]), month=9).date()
    elif ' октября' in date:
        return datetime(year=temp_date, day=int(date[0:2]), month=10).date()
    elif ' ноября' in date:
        return datetime(year=temp_date, day=int(date[0:2]), month=11).date()
    elif ' декабря' in date:
        return datetime(year=temp_date, day=int(date[0:2]), month=12).date()
    else:
        return Exception


# print(get_datetime_from_str('12 января'))
# print(get_datetime_from_str('12 ноября'))
# print(get_datetime_from_str('12 февраля'))
# print(get_datetime_from_str('12 мая'))

def get_data_from_str(date: str):
    temp_date = datetime.strptime(date, format).date()
    if temp_date.month == 1:
        return str(temp_date.day) + ' января'
    elif temp_date.month == 2:
        return str(temp_date.day) + ' февраля'
    elif temp_date.month == 3:
        return str(temp_date.day) + ' марта'
    elif temp_date.month == 4:
        return str(temp_date.day) + ' апреля'
    elif temp_date.month == 5:
        return str(temp_date.day) + ' мая'
    elif temp_date.month == 6:
        return str(temp_date.day) + ' июня'
    elif temp_date.month == 7:
        return str(temp_date.day) + ' июля'
    elif temp_date.month == 8:
        return str(temp_date.day) + ' августа'
    elif temp_date.month == 9:
        return str(temp_date.day) + ' сентября'
    elif temp_date.month == 10:
        return str(temp_date.day) + ' октября'
    elif temp_date.month == 11:
        return str(temp_date.day) + ' ноября'
    elif temp_date.month == 12:
        return str(temp_date.day) + ' декабря'
    else:
        return Exception
