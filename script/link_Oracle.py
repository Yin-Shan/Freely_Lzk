import cx_Oracle
import openpyxl
import datetime
import os,sys
import re
project_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(project_path)
from script.conf.SQL import SQL1,SQL2,SQL3
from lib.connect_mid_db import status
from script.conf.mid_bases_conf import mid_base
from script.conf.SQL import wg_sql

#filepath = os.path.abspath(os.path.dirname(__file__))
#sqlpath = os.path.join(filepath,"conf","SQL.py")
template = os.path.join(project_path,"template","每周传输配置采集结果模板.xlsx")
tm = datetime.datetime.now().strftime("%Y%m%d-%H_%M_%S")
filename = '每周传输配置采集结果-'+tm+'.xlsx'
savepath = os.path.join(project_path,"file",filename)
#    'E:\liuzhikang\python_test\\'+filename

print('查找服务器中...')
result = []
for i in range(1,22):
    result.append(status(mid_base[i][0],mid_base[i][3],mid_base[i][4],mid_base[i][1],wg_sql))
db=cx_Oracle.connect('develop/Dev2014#134@172.21.4.5/oracatt')
#db=cx_Oracle.connect('username','password','host/orcl')
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
cur.execute(SQL2)
row2 = cur.fetchone()
while row2:
    b.append(row2[0])
    row2 = cur.fetchone()
cur.execute(SQL3)
row3 = cur.fetchone()
while row3:
    c.append(row3[1])
    d.append(row3[2])
    row3 = cur.fetchone()
cur.close()
db.close()
print('查询完成')

print('正在写入Excel...')
wb1 = openpyxl.load_workbook(template)
ws1 = wb1["Sheet1"]
for i in range(len(a)):
    ws1['B' + str(i + 2)] = ws1['H' + str(i+2)].value
    ws1['H' + str(i + 2)] = a[i]
    ws1['C' + str(i + 2)] = ws1['I' + str(i+2)].value
    ws1['I' + str(i + 2)] = b[i]
    ws1['D' + str(i + 2)] = ws1['J' + str(i+2)].value
    ws1['J' + str(i + 2)] = int(c[i])
    ws1['E' + str(i + 2)] = ws1['K' + str(i+2)].value
    ws1['K' + str(i + 2)] = int(d[i])
    t = re.findall(r"(\d{4}-\d{1,2}-\d{1,2})", result[i][1])
    ws1['L'+str(i+2)] = t[0]
    ws1['M'+str(i+2)] = t[0]
    if result [i][2] == 2:
        ws1['F'+str(i+2)] = '没有查找到log.log里的ERROR字段，是一次正常的采集适配。'
    else:
        ws1['F'+str(i+2)] = '配置采集异常'
wb1.save(template)
#wb = openpyxl.load_workbook(template)
#ws1 = wb["Sheet1"]
#ws1['L23'] = result[20][1]
#ws1['L24'] = result[20][1]
#ws1['M23'] = result[20][1]
#ws1['M24'] = result[20][1]
wb1.save(savepath)
wb1.close()
print('文件保存成功，路径： '+savepath)