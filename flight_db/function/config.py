"""
place config.py in the subdirectory `function`
"""
# mysql
mysql_host = "127.0.0.1"
mysql_user = "root"
mysql_pwd = xxxx
#mysql_pwd_mac = ""
mysql_port = xxxx
#mysql_port_mac=xxxx

import mysql.connector as mc
from mysql.connector import errorcode
from sqlalchemy import create_engine, types
import pymysql

def connect_mysql(db_name):
    try:
        db = mc.connect(
            host = mysql_host,
            port = mysql_port,
            user = mysql_user,
            password = mysql_pwd,
            database=db_name
        )
    except mc.Error as e:
        print(f"something went wrong:{e}")    
        return None
    else:
        print(f"Successful connection to {db_name}")
        return db

def sqlalchemy_engine(db_name):
    try:
        engine = create_engine(f'mysql+pymysql://{mysql_user}:{mysql_pwd}@127.0.0.1:{mysql_port}/{db_name}?charset=utf8mb4')
        mysql_engine = engine.connect()
    except pymysql.Error as err:
        print(f'Connect failed: {err}')
        return None
    else:
        print(f"Successful connection to MySQL {db_name}")
        return mysql_engine
