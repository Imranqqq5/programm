# -*- coding: utf-8 -*-

import sqlite3

	
conn = sqlite3.connect(u'C:\\Users\\Имран\\Desktop\\Архив\Архив\\SchoolMainFile.sqlite')
c = conn.cursor()

c.execute("""
CREATE TABLE SchoolTable                                                                     # изменить имя.
(id INTEGER,
first_name TEXT,
last_name TEXT,
third_name TEXT,
birthday INTEGER,
iq INTEGER,
gender TEXT,
subject TEXT,
teacher TEXT,
letter TEXT,
chief TEXT,
room TEXT)

""")

c.execute('DROP SchoolTable SET data="some text" WHERE id=2')
conn.commit()

c.close()
conn.close()








