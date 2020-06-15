import pymysql,pymssql,cx_Oracle
import os,sys,datetime

project_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(project_path)
def mid_db_status(ip, user, passwd, db, sql, port=3306):
    try:
        connect = pymysql.connect(ip,user,passwd,db,port)
        cursor = connect.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        while row:
            result = row
            row = cursor.fetchone()
        cursor.close()
        connect.close()
    except Exception as e:
        print(ip,e)
    return result

def mysql(ip, user, passwd, db, *sql, port=3306):
    try:
        connect = pymysql.connect(ip, user, passwd, db, port)
        cursor = connect.cursor()
        result_list = []
        for i in sql:
            cursor.execute(i)
            row = cursor.fetchone()
            while row:
                result_list.append(row)
                row = cursor.fetchone()
        return result_list
        cursor.close()
        connect.close()
    except Exception as e:
        print(ip,e)
    return result_list

def oracle(ip, user, passwd, orcl, *sql, port='1521'):
    try:
        connect = cx_Oracle.connect(user, passwd, ip+':'+port+'/' + orcl)
        cursor = connect.cursor()
        result_list = []
        for i in sql:
            cursor.execute(i)
            row = cursor.fetchone()
            while row:
                result_list.append(row)
                row = cursor.fetchone()
        return result_list
        cursor.close()
        connect.close()
    except Exception as e:
        print(ip,e)
    return result_list

def mssql(ip, user, passwd, db, *sql, port='port=1433'):
    try:
        connect = pymssql.connect(ip, user, passwd, db, port)
        cursor = connect.cursor()
        result_list = []
        for i in sql:
            cursor.execute(i)
            row = cursor.fetchone()
            while row:
                result_list.append(row)
                row = cursor.fetchone()
        return result_list
        cursor.close()
        connect.close()
    except Exception as e:
        print(ip,e)
    return result_list

def test():

    pass

if __name__ =='__main__':
    a = mysql('172.20.8.146','root','Rot@2017','dzywdb','SELECT MAX(I_ID) FROM T_MAINTENANCE_AGG','SELECT MAX(I_ID) FROM T_MAINTENANCE_ANOMALY')
    print(type(a))
    print(a)
    b = oracle('172.21.4.5','develop','Dev2014#134','oracatt','select count(*) from t_channel','select count(*) from tbOsStaff')
    print(type(b))
    print(b)
    c = mssql('134.96.146.25', 'Jhdzyw', 'Jiaohuan*2003', 'DeviceCheck', "select count(*) from jhExc_Summary where iCountTime>'2019-12-20'","select count(*) from jhExc_Anomaly where iCountTime>'2019-12-20'")
    print(type(c))
    print(c)