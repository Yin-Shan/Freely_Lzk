import configparser
import os
import cx_Oracle
import datetime

project_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
confpath = os.path.join(project_path,"conf","account.ini")
conf = configparser.ConfigParser()
conf.read(confpath)
ip = conf.get('oracle_4.5','serverip')
user = conf.get('oracle_4.5','username')
passwd = conf.get('oracle_4.5','password')
orcl = conf.get('oracle_4.5','orcl')

db=cx_Oracle.connect(user,passwd,ip+'/'+orcl)
cur = db.cursor()
a = []
b = []
c = []
d = []
print('正在执行SQL')
cur.execute(SQL1)
row1 = cur.fetchone()
while row1:
    a.append(row1[0])
    row1 = cur.fetchone()