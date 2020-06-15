import cx_Oracle
import openpyxl
import datetime
import os,sys
import re
project_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sqlpath = os.path.join(project_path,"script","conf","test.py")
sys.path.append(project_path)
from script.conf.test import test_sql1,test_sql2

f = open(sqlpath,'r',encoding='utf-8')
f2 = open(sqlpath,'r+',encoding='utf-8')
dt = datetime.datetime.now().strftime("%Y-%m-%d")
print()
for line in f.readlines():
    if 'test_sql1' in line:
        t = re.findall(r"(\d{4}-\d{1,2}-\d{1,2})", line)
        line = line.replace(t[0],dt)
    elif 'test_sql2' in line:
        t = re.findall(r"(\d{4}-\d{1,2}-\d{1,2})", line)
        line = line.replace(t[0],dt)
    f2.write(line)
f.close()
f2.close()


