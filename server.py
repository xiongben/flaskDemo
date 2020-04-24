
# -*- coding: utf-8 -*-
import os
import paramiko
import platform

config = {
    'host': '10.30.0.41',
    'port': 22,
    'user': 'mozat',
    'pwd': 'Dgq$kmzsUsUvUbiRF',
    'server_path': '/usr/share/nginx/xiongben',
    'local_path': '/Users/mozat/learnspace/flaskDemo/flaskDemo/log.txt'
}

class SyncFiles(object):
    def __init__(self):
        # ff = open(config['local_path'])
        print "ok"

    def up_now(self):
        try:
            trans = paramiko.Transport((config['host'],22))
            trans.connect(username=config['user'],password=config['pwd'])
            sftp = paramiko.SFTPClient.from_transport(trans)
            sftp.put(localpath=config['local_path'], remotepath=config['server_path'])
            
        except Exception as e:
            print e
       
    
    def con_linux(self):
        s=paramiko.SSHClient()
        # 取消安全认证
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接linux
        s.connect(hostname=config['host'],username=config['user'],password=config['pwd'])
        # 执行命令
        stdin,stdout,stderr=s.exec_command('ls /usr/share/nginx/xiongben')
        # 读取执行结果
        result=stdout.read()
        print result
        # 关闭linux连接
        s.close()
        # 返回执行结果


res = SyncFiles()
res.up_now()
# res.con_linux()