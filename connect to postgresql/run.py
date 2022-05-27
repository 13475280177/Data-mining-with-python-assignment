import sqlalchemy
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import psycopg2

conn = psycopg2.connect(database="testdb", user="postgres", password="8712418", host="127.0.0.1", port="5432")
cur = conn.cursor()
cur.execute('''CREATE TABLE Students
       (StudentNumber INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       GENDER        CHAR(50) check (GENDER in('Male','Female','Unwilling to disclose'))
       );''')
print ("Table created successfully")

conn.commit()
conn.close()

print ("Opened database successfully")

