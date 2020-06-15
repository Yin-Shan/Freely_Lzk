import smtplib
import cx_Oracle
import os,sys,datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr

project_path = os.path.abspath(os.path.dirname(__file__))

def oracle(ip, user, passwd, orcl, tp, *sql, port='1521'):
    try:
        connect = cx_Oracle.connect(user, passwd, ip+':'+port+'/' + orcl ,encoding = "UTF-8", nencoding = "UTF-8")
        cursor = connect.cursor()
        result_list = []
        if tp == 'select':
            for a in sql:
                cursor.execute(a)
                row = cursor.fetchone()
                while row:
                    result_list.append(row)
                    row = cursor.fetchone()
            cursor.close()
            connect.close()
            return result_list
        else:
            for a in sql:
                cursor.execute(a)
                connect.commit()
            cursor.close()
            connect.close()
    except Exception as e:
        print(ip,e)

def send_mail(sender,sender_addr,receivers,cc,title,content,file_status,file_name):
    agent_host = '172.22.0.195'  # 第三方 SMTP 代理服务器地址
    agent_port = 2511
    message = MIMEMultipart()    # 创建实例
    message['From'] = formataddr((Header(sender, 'utf-8').encode(), sender_addr))
    message['To'] = ','.join(receivers.split(","))  # 多个邮箱按照逗号拼接为字符串
    if cc == None:
        pass
    else:
        message['Cc'] = ','.join(cc.split(","))
    message['Subject'] = Header(title, 'utf-8')

    # 邮件正文内容（html格式）
    message.attach(MIMEText('''
    <p>各位好：<p>
    <font> %s </font>
    '''
    % (content), 'html', 'utf-8'))
    if file_status == 1:
        file=file_name
        att_path=os.path.join(project_path,'att',file)
        att1 = MIMEText(open(att_path, 'rb').read(), 'base64', 'utf-8')    # 构造附件
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename=%s' %(file)    # filename是邮件中显示什么名字
        message.attach(att1)

    try:
        smtpObj = smtplib.SMTP(agent_host,agent_port)
        smtpObj.login(sender_addr, 'Lzk243.com')    #账号，密码
        smtpObj.sendmail(sender_addr, receivers.split(","), message.as_string())
        smtpObj.quit()
        oracle('172.21.4.58', 'develop', 'Dev2014#134', 'oracatt', 'update', 'UPDATE T_SEND_EMAIL set I_SUCCESS_STATUS = 1 where I_EMAIL_ID = %d' %(e_c[i][0]))
        print(str(e_c[i][0])+'：邮件发送成功')
    except smtplib.SMTPException as e:
        print(str(e_c[i][0])+'：邮件发送失败')
        print(e)


if __name__ == '__main__':
#    pass
    e_c = oracle('172.21.4.58','develop','Dev2014#134','oracatt', 'select','SELECT * from T_SEND_EMAIL WHERE I_SUCCESS_STATUS <> 1')
    for i in range(len(e_c)):
#        for o in range(len(e_c[i])):
#            print(o,e_c[i][o])
        if e_c[i][10] == 1:
            send_mail(e_c[i][2], e_c[i][3], e_c[i][4], e_c[i][5], e_c[i][6], e_c[i][7], e_c[i][8], e_c[i][9])
        else:
            print('没有发送任务')
    print('All done')