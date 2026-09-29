# pip install  mysql--python , pip install pymysql ,pip install psycopg2

import mysql.connector 

coonections = mysql.connector.connect(
    user = "root",
    password = "root",
    host = "localhost",
    port = 3306,
    database = "tts_da"
)

cursor = coonections.cursor()

# database create
# cursor.execute("CREATE DATABASE tts_da") 
# print("database created successfully")

# table create
'''cursor.execute(
    """CREATE TABLE IF NOT EXISTS piyush (
        id INT NOT NULL AUTO_INCREMENT, 
        name VARCHAR(255), 
        salary INT, 
        PRIMARY KEY (id))"""
)

print("table created successfully")
'''
"""
cursor.execute("INSERT INTO piyush (name,salary) VALUES ('BAHEVSH',120000)")
cursor.execute("INSERT INTO piyush (name,salary) VALUES ('JAY',130000)")
cursor.execute("INSERT INTO piyush (name,salary) VALUES ('VANSH',140000)")

coonections.commit()
"""

# row  display : 
"""
cursor.execute("SELECT * FROM piyush")

for  i in cursor:
    print(i)
"""

coonections.close()
cursor.close()

