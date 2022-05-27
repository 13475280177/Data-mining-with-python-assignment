import pandas as pd
import psycopg2
import warnings
from sqlalchemy import create_engine,text
import sqlalchemy

engine = create_engine('postgresql+psycopg2://postgres:8712418@127.0.0.1/testdb',echo=True)
db = engine.connect()

def read_record (field, name, engine):

    select = "select "+name+" from "+ field
    result = engine.execute(text(select))
    print(result.keys())
    print(result.fetchall())
def update_record (name, details, engine):
    update = "update "+name+" set "+details
    result = engine.execute(text(update))
    print(result.rowcount)
def write_record (field ,name, newvalue, engine):
    insert = "insert into "+field+"("+name+") "+"values("+newvalue+")"
    result = engine.execute(text(insert))
    print(result.rowcount)

def read_dataset (field,engine):
    read = "SELECT * FROM "+field
    result = engine.execute(text(read))
    print(result.fetchall())
    print("read success")
def write_dataset (name, dataset, engine):
    write = "create table "+name+dataset
    result= engine.execute(text(write))
def list_datasets (engine):
    show = "SELECT *FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema'"
    result = engine.execute(text(show))
    h = pd.DataFrame(result)
    print(h[1])
    print(result.rowcount)


# read_record("students","gender",db)
# write_record("students","studentnumber","'""20218848""'",db)
list_datasets(db)
db.close()

# conn = psycopg2.connect(database="testdb", user="postgres", password="8712418", host="127.0.0.1", port="5432")
# cur = conn.cursor()
# cur.execute('''COPY students(studentnumber,name,age,gender)
# FROM 'S:\Data minng\connect to postgresql\specs\input_DW_data.csv'
# DELIMITER ','
# CSV HEADER;''')
# print ("Table copied successfully")
#
# conn.commit()
# conn.close()
# engine = create_engine(
#     'postgresql+psycopg2://'
# )
# def read_record (field, name, engine):
#
# def write_record (name, details, engine):
#
# def update_record (field name, new value, engine):
#
#
# def read_dataset (name, engine):
#
# def write_dataset (name, dataset, engine):
#
# def list_datasets (engine):



