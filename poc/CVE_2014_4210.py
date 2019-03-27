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
    url='http://' + str(ur)+':'+str(port)+'/uddiexplorer/'
    try:
        r = requests.get(url,timeout=5, headers=headers)
        return r.status_code
    except:
        fw = open(logname, 'a')
        fw.write("[*]{}UDDI模块路径响应超时\n".format(url))
        fw.close()
        return 0

def run(url,port):
    if islive(url,port)==200:
        fw = open(logname, 'a')
        fw.write('[+]目标weblogic存在UDDI组件!路径为:{}\n'.format('http://' + str(url)+':'+str(port)+'/uddiexplorer/'))
        fw.close()
    else:
        fw = open(logname, 'a')
        fw.write("[-]目标weblogic UDDI组件默认路径不存在!\n".format(url,port))
        fw.close()

if __name__=="__main__":
    url = sys.argv[1]
    port = int(sys.argv[2])
    run(url,port)