from base import BaseModel, BasePersonModel, BaseClassModel, BaseEduPlan, BaseSubject


class Subject(BaseModel, BasePersonModel, BaseClassModel, BaseEduPlan, BaseSubject):
	
	def __init__(self, id, title):
        self.id = id
        self.title = title
