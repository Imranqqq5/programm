# coding: utf-8 
from base import BaseModel, BasePersonModel, BaseClassModel, BaseEduPlan, BaseSubject


class Pupil(BaseModel, BasePersonModel, BaseClassModel, BaseEduPlan, BaseSubject):
    """
    Класс для учеников
    """

    iq = None

    def __init__(self, id, first_name, last_name, third_name, birthday, iq, gender):
        BaseModel.__init__(self, id)
        BasePersonModel.__init__(self, first_name, last_name, third_name, birthday, gender)
        self.iq = iq
