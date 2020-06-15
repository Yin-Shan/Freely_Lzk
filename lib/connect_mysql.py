import pymysql
import configparser
import os,sys

project_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
confpath = os.path.join(project_path,"conf","account.ini")
conf = configparser.ConfigParser()
conf.read(confpath)
ip = conf.get('mysql_146','serverip')
user = conf.get('mysql_146','username')
passwd = conf.get('mysql_146','password')
db = conf.get('mysql_146','database')

def connect_mysql(ip,user,passwd,db,sql):
    conn = pymysql.connect(ip,user,passwd,db)
    cursor = conn.cursor()
    cursor.execute(sql)
    row = cursor.fetchone()
    while row:
        print(row)
        row = cursor.fetchone()
    return row
    conn.commit()
    cursor.close()
    conn.close()
