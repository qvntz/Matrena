import sqlalchemy.orm
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine

Base = declarative_base()
engine = create_engine('sqlite:///db.sqlite')
# engine = create_engine('postgresql://localhost:5432/MFC')

session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base.query = session.query_property()


# Tables
# ----------------------------------------------------------------------------------------------------------------------

class Orders(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    status = Column(String)
    total_id = Column(Integer)


class MFC(Base):
    __tablename__ = 'mfcs'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    namelower = Column(String)
    x = Column(Float)
    y = Column(Float)


class Times(Base):
    __tablename__ = 'timeses'

    id = Column(Integer, primary_key=True)
    time = Column(String, nullable=False)
    username = Column(String, default='N')
    name = Column(String)
    surname = Column(String)
    telephone = Column(String)
    mfc_id = Column(Integer, ForeignKey('mfcs.id'))
    mfcs = sqlalchemy.orm.relationship("MFC", backref='timeses')


# Func
# -----------------------------------------------------------------------------------------------------------------------

def add_MFC():
    listmfc = []
    mfc = MFC(
        name='МФЦ Адмиралтейского района',
        x=59.92361013193151, y=30.284494930685902)
    mfc.timeses = [Times(time='16.45'),
                   Times(time='17.30'),
                   Times(time='18.00'),
                   Times(time='13.40')
                   ]

    listmfc.append(mfc)
    mfc = MFC(
        name='МФЦ Василеостровского района',
        x=59.943641751175015, y=30.22640714260935)
    mfc.timeses = [Times(time='11.25'),
                   Times(time='12.30'),
                   Times(time='13.00'),
                   Times(time='13.10'),
                   Times(time='13.15'),
                   Times(time='13.30'),
                   Times(time='13.45'),
                   ]

    listmfc.append(mfc)
    mfc = MFC(name='МФЦ Выборгского района',
              x=60.05497791451475, y=30.361088969600022)
    mfc.timeses = [Times(time='13.25'),
                   Times(time='14.30'),
                   Times(time='15.00'),
                   Times(time='15.10'),
                   Times(time='15.15'),
                   Times(time='15.30'),
                   Times(time='15.45'),
                   ]

    listmfc.append(mfc)
    mfc = MFC(name='МФЦ Калининского района',
              x=59.92361013193151, y=30.564494930685902)
    mfc.timeses = [Times(time='16.45'),
                   Times(time='17.30'),
                   Times(time='18.00'),
                   Times(time='13.40'),
                   ]

    listmfc.append(mfc)
    mfc = MFC(name='МФЦ Кировского района',
              x=59.83891662078884, y=30.270769929111836)
    mfc.timeses = [Times(time='16.45'),
                   Times(time='17.30'),
                   Times(time='18.00'),
                   Times(time='13.40'),
                   ]

    listmfc.append(mfc)
    mfc = MFC(name='МФЦ Колпинского района',
              x=59.813639179596414, y=30.577323913767763)
    mfc.timeses = [Times(time='16.45'),
                   Times(time='17.30'),
                   Times(time='15.00'),
                   Times(time='12.00'),
                   Times(time='13.40'),
                   ]

    listmfc.append(mfc)
    mfc = MFC(
        name='МФЦ Красногвардейского района',
        x=59.93892746842608, y=30.485850727266175)
    mfc.timeses = [Times(time='16.45'),
                   Times(time='17.30'),
                   Times(time='15.00'),
                   Times(time='12.00'),
                   Times(time='13.40'),
                   ]

    listmfc.append(mfc)
    mfc = MFC(
        name='МФЦ Красносельского района',
        x=59.744836296851894, y=30.07703195609313)
    mfc.timeses = [Times(time='14.45'),
                   Times(time='15.30'),
                   Times(time='15.00'),
                   Times(time='12.00'),
                   Times(time='13.40'),
                   ]

    listmfc.append(mfc)
    mfc = MFC(
        name='МФЦ Кронштадтского района',
        x=59.991916419905, y=29.755934540761377)
    mfc.timeses = [Times(time='14.45'),
                   Times(time='15.30'),
                   Times(time='15.00'),
                   Times(time='12.00'),
                   Times(time='13.40'),
                   ]

    listmfc.append(mfc)
    mfc = MFC(name='МФЦ Курортного района',
              x=60.19906778845881, y=29.70586894077081)
    mfc.timeses = [Times(time='14.45'),
                   Times(time='15.30'),
                   Times(time='15.00'),
                   Times(time='12.00'),
                   Times(time='13.40'),
                   ]

    listmfc.append(mfc)
    mfc = MFC(name='МФЦ Московского района',
              x=59.8583669546415, y=30.306453911919565)
    mfc.timeses = [Times(time='14.45'),
                   Times(time='15.30'),
                   Times(time='15.00'),
                   Times(time='12.00'),
                   Times(time='13.40'),
                   ]

    listmfc.append(mfc)

    mfc = MFC(name='МФЦ Невского района',
              x=59.87630310236257, y=30.43263680822008)
    mfc.timeses = [Times(time='14.45'),
                   Times(time='15.30'),
                   Times(time='15.00'),
                   Times(time='12.00'),
                   Times(time='13.40'),
                   ]

    listmfc.append(mfc)
    mfc = MFC(
        name='МФЦ Петроградского района',
        x=59.960399623978994, y=30.278036811924235)
    mfc.timeses = [Times(time='14.45'),
                   Times(time='15.30'),
                   Times(time='15.00'),
                   Times(time='12.00'),
                   Times(time='13.40'),
                   ]

    listmfc.append(mfc)

    mfc = MFC(
        name='МФЦ Петродворцового района',
        x=59.908466, y=29.775127)
    mfc.timeses = [Times(time='14.45'),
                   Times(time='15.30'),
                   Times(time='15.00'),
                   Times(time='12.00'),
                   Times(time='13.40'),
                   ]

    listmfc.append(mfc)
    mfc = MFC(name='МФЦ Приморского района',
              x=60.032074, y=30.294452)
    mfc.timeses = [Times(time='14.45'),
                   Times(time='15.30'),
                   Times(time='15.00'),
                   Times(time='12.00'),
                   Times(time='13.40'),
                   ]

    listmfc.append(mfc)
    mfc = MFC(name='МФЦ Пушкинского района',
              x=59.804165, y=30.377996)
    mfc.timeses = [Times(time='14.45'),
                   Times(time='15.30'),
                   Times(time='15.00'),
                   Times(time='12.00'),
                   Times(time='13.40'),
                   ]

    listmfc.append(mfc)
    mfc = MFC(name='МФЦ Фрунзенского района',
              x=59.855236, y=30.367818)
    mfc.timeses = [Times(time='14.45'),
                   Times(time='15.30'),
                   Times(time='15.00'),
                   Times(time='12.00'),
                   Times(time='13.40'),
                   ]

    listmfc.append(mfc)

    session.add_all(listmfc)
    session.commit()


# Полностью отлчистить базу данных
def delete_DB():
    Base.metadata.drop_all(engine)


Base.metadata.create_all(bind=engine)
# add_MFC()
# delete_DB()
