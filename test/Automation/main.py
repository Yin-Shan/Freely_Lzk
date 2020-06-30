import paramiko
import re
import time

class Linux():
    def __init__(self, ip, port, username, password, timeout=10):    # 通过IP, 用户名，密码，超时时间初始化一个远程Linux主机
        self.ip = ip
        self.username = username
        self.password = str(password)
        self.timeout = timeout
        self.port = port
            # transport和chanel
        self.tran = ''
        self.chan = ''
        self.sshc = ''

    def trans(self):    # 调用该方法连接远程主机
        try:
            self.tran = paramiko.Transport(sock=(self.ip, self.port))
            self.tran.connect(username=self.username, password=self.password)


            self.chan = self.tran.open_session()
            self.chan.settimeout(self.timeout)
            self.chan.get_pty()
            self.chan.invoke_shell()
            return
        except Exception as e:
            print(e)
            exit(1)

    def ssh(self):
        try:
            self.sshc = paramiko.SSHClient()
            self.sshc.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.sshc.connect(hostname=self.ip, port=self.port, username=self.username, password=self.password, timeout=self.timeout)
            self.chan = self.sshc.invoke_shell()
            return
        except Exception as e:
            print(e)
            exit(1)

    def su_root(self,passwd):
        resp = self.chan.recv(65535)
        self.chan.send("su -\n")
        time.sleep(0.5)
        self.chan.send("%s\n"%(passwd))
        buff=''
        while not (buff.endswith('$ ') or buff.endswith('# ')):    # 通过命令执行提示符来判断命令是否执行完成
            time.sleep(0.2)
            resp = self.chan.recv(65535)
            try:
                buff += resp.decode('gb18030')
            except:
                buff += resp.decode('utf-8')
            print(buff)
            return

    def send(self, cmd):    # 发送要执行的命令
        self.chan.send("%s\n"%(cmd))    #cmd += '\n' #内置回车
        buff=''
        while not (buff.endswith('$ ') or buff.endswith('# ')):    # 通过命令执行提示符来判断命令是否执行完成
            time.sleep(0.1)
            resp = self.chan.recv(65535)
            try:
                buff += resp.decode('gb18030')
            except:
                buff += resp.decode('utf-8')
            print(buff)
        return(buff)

    def upload(self):
        pass

    def download(self):
        pass

    def close(self):    # 断开连接
        self.sshc.close()
        self.chan.close()
        #self.tran.close()


if __name__ == '__main__':
    host = Linux('193.168.11.110', 22, 'cat', '1')
    host.ssh()    #ip,用户,密码,超时时间(可选),端口(默认22)
    host.su_root('0')
    #host.send('cd /home/cattsoft')
    host.send('ls')
    #host.send('ls --color=never')   #解决cmd杂码
    host.close()