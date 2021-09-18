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
    # print(temp_date)
    # return get_data_from_str(str(temp_date))


format = '%Y-%m-%d'


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

