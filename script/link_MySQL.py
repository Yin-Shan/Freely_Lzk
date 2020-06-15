import pymysql

def max_iid_agg():
    host='172.20.8.146'
    user='root'
    password='Rot@2017'
    database='dzywdb'
    conn = pymysql.connect(host,user,password,database,port=3306)
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(I_ID) FROM T_MAINTENANCE_AGG")
    row = cursor.fetchone()
    while row:
#        print(row)
        row = cursor.fetchone()
    return row
    conn.commit()
    cursor.close()
    conn.close()

def max_iid_anomaly():
    host='172.20.8.146'
    user='root'
    password='Rot@2017'
    database='dzywdb'
    conn = pymysql.connect(host,user,password,database,port=3306)
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(I_ID) FROM T_MAINTENANCE_ANOMALY")
    row = cursor.fetchone()
    while row:
#        print(row)
        row = cursor.fetchone()
    return row
    conn.commit()
    cursor.close()
    conn.close()

def insert_sql(sql):
    host='172.20.8.146'
    user='root'
    password='Rot@2017'
    database='dzywdb'
    conn = pymysql.connect(host,user,password,database,port=3306)
    cursor = conn.cursor()
    cursor.execute(sql)
    row = cursor.fetchone()
    while row:
        print(row)
        row = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()