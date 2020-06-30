import paramiko
import time
from program_dict import caiji,shipei,shipei_distinct,caiji_distinct,caiji_shipei_distinct,ipa
#                        采集程序，适配程序，适配机IP，采集机IP，采集和适配机IP，所有机器IP ↑
err_list = []
done_list=[]
def chip(no,ip,lj):
    global done_list
    global err_list
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if ip == '172.22.0.172':
            ssh.connect(hostname=ip, port=22, username='cattsoft', password='Cat@4321', timeout=10)
        else:
            ssh.connect(hostname=ip, port=22, username='cattsoft', password='Cat@1234', timeout=10)
        channel = ssh.invoke_shell()
        resp = channel.recv(65535)
        channel.settimeout(8)           #设置超时跳过时间
        #channel.send("su -\n")          #切root执行
        #time.sleep(2)                   #切root执行
        #if ip == '172.22.0.172':        #切root执行
        #    channel.send("Rot@4321\n")  #切root执行
        #else:                           #切root执行
        #    channel.send("Rot@1234\n")  #切root执行
        #channel.send("mkdir 20200519\n")
        #channel.send('d=$(pwd)\n')
        channel.send("cd %s\n"%(lj))
        #channel.send("sh stop.sh\n")
        channel.send("sh start.sh\n")
        #channel.send("cat stop.sh\n")
        #channel.send("ls --color=never\n")
        #channel.send('a=$(pwd);a=${a##*cattsoft\/};b=${a//\//#};c=${a##*\/}\n')
        #channel.send("curl -s -L 'http://172.20.7.138/agent/download?k=2727be12f371dba4f0d9124dfeb07667bf346096&group=22&protocol=0' | bash\n")
        #channel.send('tar -czvf $d\/20200518\/%s#$b.tar.gz --exclude=logs --exclude=state --exclude=out/state --exclude=*.gz --exclude=*.log --exclude=F150 --exclude=S1240 --exclude=C08I --exclude=EWSD --exclude=data --exclude=SPS --exclude=log --exclude=OTHER --exclude=report --exclude=*.zip $c\n'%(no))
        #if no in [33,34,35,36,47,52,53,54,55,56,57,58,59,63,64,65,66,67,68,69,70,160,162,165]:   #启动脚本里没有杀进程的
        #    channel.send('cat _\t\n')
        #    channel.send('echo -----\n')
        #    channel.send('cat start.s\t\n')
        #else:
        #    channel.send('cat start.s\t\n')
        #channel.send("ps -ef |grep -v grep|grep %s\n"%(jc))
        #channel.send("sed -n '/znwgbk01/p' /etc/hosts\n")
        #channel.send("sed -i '/znwgbk01/c\\172.13.1.116\\tznwgbk01' /etc/hosts\n")  #切到备用环境（采集和适配机）
        #channel.send("sed -i '/znwgbk01/c\\172.13.0.101\\tznwgbk01' /etc/hosts\n")  #切回正式环境（采集和适配机）
        buff=''
        while not (buff.endswith('$ ') or buff.endswith('# ')):
            time.sleep(0.2)
            resp = channel.recv(65535)
            try:
                buff += resp.decode('gb18030')
            except Exception as b:
                buff += resp.decode('gb2312')
            except:
                buff += resp.decode('utf-8')
        print(buff)
        my_file = open('done_list.txt', 'a')
        my_file.write(str(no)+':'+str(ip)+'\n'+str(buff)+'\n')
        my_file.close()
        ssh.close()
    except Exception as e:
        print(e)
        print(type(e))
        my_file = open('err_list.txt', 'a')
        my_file.write(str(no)+':'+str(ip)+'\n'+str(type(e))+'\n')
        my_file.close()
        ssh.close()

if __name__ == '__main__':
    #for i in range(1, 17):   #程序
    #    print(i,shipei_distinct[i][0])
    #    chip(i,shipei_distinct[i][0])
    
    for i in range(1,170):    #适配程序(22跳过，33,34,35,36,47,52,53,54,55,56,57,58,59,63,64,65,66,67,68,69,70,160,162,165没有自杀，要先停止)
        if i in (22,33,34,35,36,47,52,53,54,55,56,57,58,59,63,64,65,66,67,68,69,70,160,162,165):
            pass
        else:
            print(i,shipei[i][0])
            chip(i,shipei[i][0],shipei[i][1])

    #for i in range(1,170):   #采集程序(24跳过，19,20,21,22,41,48,49,50,51,61,62,72,88,89,108,109,117,118,119,120连不上，)
    #    elif i in (24,19,20,21,22,41,48,49,50,51,61,62,72,88,89,108,109,117,118,119,120):
    #        pass
    #    else:
    #        print(i, caiji[i][0])
    #        chip(i, caiji[i][0], caiji[i][1])
