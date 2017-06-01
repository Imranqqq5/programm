from base import BaseModel, BasePersonModel, BaseClassModel, BaseEduPlan, BaseSubject


class EduPlan(BaseModel, BasePersonModel, BaseClassModel, BaseEduPlan, BaseSubject):

    def __init__(self, id, subject_id, teacher_id, edu_class_id):
        self.id = id
        self.subject_id = subject_id
        self.teacher_id = teacher_id
        self.edu_class_id = edu_class_id
	

