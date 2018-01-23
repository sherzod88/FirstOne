# -*- coding: utf-8 -*-
"""

"""

import pymysql

db = pymysql.connect(host ='localhost',
                            user='root',
                            password='',
                            db='tutorial_database2')

cursor = db.cursor()

sql_create_table ="""
CREATE TABLE PERSON (
ID INT NOT NULL, 
FIRST_NAME CHAR(20) NOT NULL, 
LAST_NAME CHAR(20),
AGE INT, 
SEC CHAR(1),
PRIMARY KEY (ID))"""
        
cursor.execute(sql_create_table)

db.close()