import pymysql
import os,sys
import datetime
project_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(project_path)
def status(ip,user,passwd,db,sql):
    try:
        conn = pymysql.connect(ip,user,passwd,db)
        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        while row:
            result = row
            row = cursor.fetchone()
        cursor.close()
        conn.close()
    except Exception as e:
        print(ip,e)
    return result




