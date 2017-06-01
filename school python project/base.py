class BaseModel(object):

    id = None

    def __init__(self, id=None):
        self.id = id

    @classmethod
    def get_table_name(cls):
        return '{}s'.format(cls.__name__.lower())

    def update(self):
        sql_format_str = 'UPDATE {} SET {} WHERE id={};'
        _data = []
        for key, value in self.__dict__.items():
            if key == 'id':
                continue
            pattern = '{}="{}"'.format(key, value)
            _data.append(pattern)

        sql_format_str = sql_format_str.format(self.get_table_name(), ','.join(_data), self.id)
        print(sql_format_str)
        # sqlite.exec(sql_format_str)

    def create(self):
    sql_format_str = 'INSERT INTO{} VALUES{};'
    _data = []
	for key, value in self.__dict__.items():
	    if key == 'id':
                continue
            pattern = '{}="{}"'.format(key, value)
            _data.append(pattern)

        sql_format_str = sql_format_str.format(self.get_table_name(), ','.join(_data), self.id)
        print(sql_format_str)   

		
    def delete(self):
        sql_format_str = 'DROP TABLE{};'
        
	    

    @classmethod
    def select(self, **kwargs):
        sql_format_str = 'SELECT * FROM {} WHERE {};' #  Посмотри LIMIT 1
        
        _data = []
        for key, value in kwargs.items():
            pattern = '{}="{}"'.format(key, value)
            _data.append(pattern)
        sql_format_str = sql_format_str.format(self.get_table_name(), ' AND '.join(_data), self.id)
        print(sql_format_str)


class BasePersonModel(object):

    first_name = None
    last_name = None
    third_name = None
    birthday = None
    gender = None

    def __init__(self, first_name, last_name, third_name, birthday, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.third_name = third_name
        self.birthday = birthday
        self.gender = gender

		
class BaseClassModel(object):

    id = None
    number = None
    letter = None
    chief = None
    room = None
	
	def __init__(self, id, number, letter, chief, room):
        self.id = id
        self.number = number
        self.letter = letter
        self.chief = chief
        self.room = room
    
	
class BaseEduPlan(object):

    id = None
    subject_id = None # ссылка на другой объект. UUID
    teacher_id = None
    edu_class_id = None
	
	def __init__(self, id, subject_id, teacher_id, edu_class_id):
        self.id = id
        self.subject_id = subject_id
        self.teacher_id = teacher_id
        self.edu_class_id = edu_class_id
		
		
class BaseSubject(object):

    id = None
    title = None        
	
	def __init__(self, id, title):
        self.id = id
        self.title = title
        
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	