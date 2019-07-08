#!/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\

'''
import logging
import re
from multiprocessing import Pool, Manager
import poc.Console
import poc.CVE_2014_4210
import poc.CVE_2016_0638
import poc.CVE_2016_3510
import poc.CVE_2017_3248
import poc.CVE_2017_3506
import poc.CVE_2017_10271
import poc.CVE_2018_2628
import poc.CVE_2018_2893
import poc.CVE_2018_2894
import poc.CVE_2019_2725
import poc.CVE_2019_2729

logging.basicConfig(filename='Weblogic.log',
                    format='%(asctime)s %(message)s',
                    filemode="w", level=logging.INFO)

version = "2.1"
banner='''
__        __   _     _             _        ____                  
\ \      / /__| |__ | | ___   __ _(_) ___  / ___|  ___ __ _ _ __  
 \ \ /\ / / _ \ '_ \| |/ _ \ / _` | |/ __| \___ \ / __/ _` | '_ \ 
  \ V  V /  __/ |_) | | (_) | (_| | | (__   ___) | (_| (_| | | | |
   \_/\_/ \___|_.__/|_|\___/ \__, |_|\___| |____/ \___\__,_|_| |_|
                             |___/ 
                             By Tide_RabbitMask | V {} 
'''.format(version)

def board():
    print (banner)
    print('Welcome To WeblogicScan !!!\nWhoami：rabbitmask.github.io\n')
    #懒得做交互了，大家自行变更path
    path='ipresult.txt'
    poolmana(path)


def poolmana(path):
    p = Pool(10)
    q = Manager().Queue()
    fr = open(path, 'r')
    rtar = fr.readlines()
    fr.close()
    for i in range(len(rtar)):
        ruleip=re.compile('(.*?):')
        rip =(ruleip.findall(rtar[i]))[0]
        ruleport=re.compile(':(.*)')
        rport=ruleport.findall(rtar[i])[0]
        p.apply_async(work,args=(rip,rport,q,))
    p.close()
    p.join()
    print('>>>>>End of task\n')


def work(rip,rport,q):
    print ('[*]任务加载成功，目标:{}:{}\n'.format(rip,rport))
    try:
        poc.Console.run(rip, rport)
    except:
        logging.info ("[-]Target Weblogic console address not found.")

    try:
        poc.CVE_2014_4210.run(rip,rport)
    except:
        logging.info ("[-]CVE_2014_4210 not detected.")

    try:
        poc.CVE_2016_0638.run(rip,rport,0)
    except:
        logging.info ("[-]CVE_2016_0638 not detected.")

    try:
        poc.CVE_2016_3510.run(rip, rport, 0)
    except:
        logging.info ("[-]CVE_2016_3510 not detected.")

    try:
        poc.CVE_2017_3248.run(rip, rport, 0)
    except:
        logging.info ("[-]CVE_2017_3248 not detected.")

    try:
        poc.CVE_2017_3506.run(rip, rport, 0)
    except:
        logging.info ("[-]CVE_2017_3506 not detected.")

    try:
        poc.CVE_2017_10271.run(rip, rport, 0)
    except:
        logging.info("[-]CVE_2017_10271 not detected.")

    try:
        poc.CVE_2018_2628.run(rip, rport, 0)
    except:
        logging.info("[-]CVE_2018_2628 not detected.")

    try:
        poc.CVE_2018_2893.run(rip, rport, 0)
    except:
        logging.info("[-]CVE_2018_2893 not detected.")

    try:
        poc.CVE_2018_2894.run(rip, rport, 0)
    except:
        logging.info("[-]CVE_2018_2894 not detected.")

    try:
        poc.CVE_2019_2725.run(rip, rport, 0)
    except:
        logging.info("[-]CVE_2019_2725 not detected.")

    try:
        poc.CVE_2019_2729.run(rip, rport, 0)
    except:
        logging.info("[-]CVE_2019_2729 not detected.")

    print ('[*]任务检测完成，目标:{}:{}\n'.format(rip,rport))
    q.put(rip)

def run():
    board()

if __name__ == '__main__':
    run()
