# coding: utf-8
from base import BaseModel, BasePersonModel, BaseClassModel, BaseEduPlan, BaseSubject


class Teacher(BaseModel, BasePersonModel, BaseClassModel, BaseEduPlan, BaseSubject):

    def __init__(self, id, first_name, last_name, third_name, birthday, iq, gender):
        BaseModel.__init__(self, id)
        BasePersonModel.__init__(self, first_name, last_name, third_name, birthday, gender)

# teacher = Teacher(10, 'Имран', 'X', 'Y', '2009', 150, 'man')