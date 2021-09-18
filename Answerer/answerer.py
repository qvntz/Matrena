from typing import Optional

# fix import
import pandas as pd
from Answerer.similarityMatchingSkill import SimilarityMatchingSkill
from definitions import LEARNING_DATA_FILE, COMPLETED_FAQ_FILE

faqCSVPath = LEARNING_DATA_FILE
completedFaq = COMPLETED_FAQ_FILE


class Answerer(object):

    def __init__(self, data_path: Optional[str] = faqCSVPath, config_type: Optional[str] = 'tfidf_autofaq',
                 x_col_name: Optional[str] = 'Вопрос', y_col_name: Optional[str] = 'Ответ',
                 save_load_path: Optional[str] = './answer_skill',
                 edit_dict: Optional[dict] = None, train: Optional[bool] = False):
        try:
            self.__completedAnswersDf = pd.read_csv(completedFaq)
            self.__rawFAQDf = pd.read_csv(faqCSVPath)
            # todo add 'загран' in model like 'заграничный'
            # todo предобучить на твиттере
            self.__faq_skill = SimilarityMatchingSkill(data_path, config_type=config_type, x_col_name=x_col_name,
                                                       y_col_name=y_col_name,
                                                       train=train, save_load_path=save_load_path,
                                                       edit_dict=edit_dict)
        except Exception as e:
            print(e)

    """Logic be like.

            Args:
                question :

            Returns:
                .
            """

    def giveAnswer(self, question: Optional[str] = None) -> pd.DataFrame:
        if question is None:
            raise TypeError("There's no question")
        questions = [question]
        answers, score = self.__faq_skill(questions, [], [])
        df_filter = self.__rawFAQDf['Ответ'].isin(answers)
        answer = self.__completedAnswersDf[df_filter]
        dfFilterForGetAll = self.__completedAnswersDf['Вопрос'].isin(answer['Вопрос'])
        answers = self.__completedAnswersDf[dfFilterForGetAll]
        return answers
