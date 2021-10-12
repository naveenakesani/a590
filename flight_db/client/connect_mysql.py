import config, os
import pandas as pd
# pip install mysql-connector-python
# pip install pymysql
# pip install sqlalchemy
import mysql.connector as mc
from mysql.connector import errorcode

try:
    db = mc.connect(
        host = config.mysql_host,
        port = config.mysql_port,
        user = config.mysql_user,
        password = config.mysql_pwd,
        database="flight2"
    )
except mc.Error as e:
    print(f"something went wrong:{e}")    
else:
    print("Success")

airlines_df = pd.read_sql("select * from airline", db)    
airlines_df.info()

dir = "client" #subfolder
file_name = "list_airlines" #filename
fpath = os.path.join(dir, f"{file_name}.csv")
with open(fpath, "w", encoding="utf-8" ) as f:
    airlines_df.to_csv(f, index=False, line_terminator='\n')

db.close()    
