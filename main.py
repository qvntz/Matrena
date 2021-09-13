from answerer import Answerer
from pandas import DataFrame

if __name__ == '__main__':
    answerer = Answerer()
    df = answerer.giveAnswer('Пособие')
    print(df)
