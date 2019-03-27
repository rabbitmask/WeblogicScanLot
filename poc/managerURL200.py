#!/usr/bin/env python
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _    
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   < 
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\

'''
import sys
import requests

logname='weblogic.log'
headers = {'user-agent': 'ceshi/0.0.1'}

def islive(ur,port):
    url='http://' + str(ur)+':'+str(port)+'/console/login/LoginForm.jsp'
    try:
        r = requests.get(url,timeout=5, headers=headers)
        return r.status_code
    except:
        fw = open(logname, 'a')
        fw.write("[*]{}控制台路径响应超时\n".format(url))
        fw.close()
        return 0

def run(url,port):
    if islive(url,port)==200:
        u='http://' + str(url)+':'+str(port)+'/console/login/LoginForm.jsp'
        fw = open(logname, 'a')
        fw.write("[+]目标weblogic控制台地址暴露!路径为:{}\n".format(u))
        fw.close()
    else:
        fw = open(logname, 'a')
        fw.write("[-]{}:{}控制台地址未找到!\n".format(url,port))
        fw.close()

if __name__=="__main__":
    url = sys.argv[1]
    port = int(sys.argv[2])
    run(url,port)
    # run('127.0.0.1',7001)