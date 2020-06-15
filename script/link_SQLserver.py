import pymssql

def select_summary:
    serverIP = '134.96.146.25'
    userName = 'Jhdzyw'
    passWord = 'Jiaohuan*2003'
    dateBase = 'DeviceCheck'
    link = pymssql.connect(serverIP,userName,passWord,dateBase,port='1433')
    cursor = link.cursor()
    cursor.execute("select * from jhExc_Summary where iCountTime>'2019-12-2'")
    row = cursor.fetchone()
    while row:
        print(row)
        row = cursor.fetchone()
    cursor.close()
    link.close()

def select_anomaly:
    serverIP = '134.96.146.25'
    userName = 'Jhdzyw'
    passWord = 'Jiaohuan*2003'
    dateBase = 'DeviceCheck'
    link = pymssql.connect(serverIP, userName, passWord, dateBase, port='1433')
    cursor = link.cursor()
    cursor.execute("select * from jhExc_Summary where iCountTime>'2019-12-2'")
    row = cursor.fetchone()
    while row:
        print(row)
        row = cursor.fetchone()
    cursor.close()
    link.close()