from answererControl import AnswererControl
from DB.MakeDB import add_MFC,delete_DB, Base , engine , post_MFC
from DB.UpdateDB import put_new_timeses, delete_past_time
from DB.FuctionsDB import *



delete_DB()
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
setRecord(datas[0] , timese[0], 'МФЦ Адмиралтейского района' ,'Andrey_Varan', 'Andrey ',  '89098172313' )
print('getRecordByName')
print(getRecordByName('Andrey '))
print('getRecordByUsername')
print(getRecordByUsername('Andrey_Varan'))
# 'Perevoshikov ',