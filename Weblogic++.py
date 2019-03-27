#!/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\

'''
from multiprocessing import Pool, Manager
import poc.managerURL200
import poc.CVE_2014_4210
import poc.CVE_2016_0638
import poc.CVE_2016_3510
import poc.CVE_2017_3248
import poc.CVE_2018_2628
import poc.CVE_2018_2893


version = "1.1"
banner='''
__        __   _     _             _                    
\ \      / /__| |__ | | ___   __ _(_) ___     _     _   
 \ \ /\ / / _ \ '_ \| |/ _ \ / _` | |/ __|  _| |_ _| |_ 
  \ V  V /  __/ |_) | | (_) | (_| | | (__  |_   _ _   _|
   \_/\_/ \___|_.__/|_|\___/ \__, |_|\___|   |_|   |_|  
                             |___/    
                             
                             By Tide_RabbitMask | V {} 
'''.format(version)

def board():
    print (banner)
    print ('Welcome To Weblogic++ !!\n')
    #懒得做交互了，大家自行变更path
    path='ipresult.txt'
    poolmana(path)


def poolmana(path):
    p = Pool(10)
    q = Manager().Queue()
    fr = open(path, 'r')
    rips = fr.readlines()
    fr.close()
    for i in range(len(rips)):
        rip = rips[i]
        rip = rip.replace("\n", '')
        p.apply_async(work, args=(rip,7001,q))
    p.close()
    p.join()
    print('>>>>>End of task\n')


def work(rip,rport,q):
    print (u'[*]任务加载成功，目标:{}:{}\n'.format(rip,rport))
    try:
        poc.managerURL200.run(rip, rport)
    except:
        pass
    try:
        poc.CVE_2014_4210.run(rip,rport)
    except:
        pass
    try:
        poc.CVE_2016_0638.run(rip,rport,0)
    except:
        pass
    try:
        poc.CVE_2016_3510.run(rip, rport, 0)
    except:
        pass
    try:
        poc.CVE_2017_3248.run(rip, rport, 0)
    except:
        pass
    try:
        poc.CVE_2018_2628.run(rip, rport, 0)
    except:
        pass
    try:
        poc.CVE_2018_2893.run(rip, rport, 0)
    except:
        pass
    print (u'[*]任务检测完成，目标:{}:{}\n'.format(rip,rport))
    q.put(rip)

def run():
    board()

if __name__ == '__main__':
    run()
