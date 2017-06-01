from base import BaseModel, BasePersonModel, BaseClassModel, BaseEduPlan, BaseSubject


class EduClass(BaseModel, BasePersonModel, BaseClassModel, BaseEduPlan, BaseSubject):

    def __init__(self, id, number, letter, chief, room):
        BaseModel.__init__(self, id)
        BasePersonModel.__init__(self, first_name, last_name, third_name, birthday, gender)