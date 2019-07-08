    软件作者：Tide_RabbitMask
    免责声明：Pia!(ｏ ‵-′)ノ”(ノ﹏<。)
    本工具仅用于安全测试，请勿用于非法使用，要乖哦~
        
    V2.1简介：
    提供weblogic批量检测功能，收录几乎全部weblogic历史漏洞。
    【没有遇到过weblogic批量检测工具的小朋友举起你的爪爪！】

	PS：
	综上:V2.*系列不是V1.*的升级版，只是多进程批量版本。
	对于当个目标站点的检测，依然推荐您使用V1.*系列。
	
	V 2.*系列特色：
        1.多进程任务高效并发
        2.简洁直观的监控界面
        3.健全的日志记录功能
        4.健全的异常处理机制
	
	V 2.*功能详情：
        #控制台路径泄露
        Console  
        
        #SSRF：
        CVE-2014-4210      
        
        #JAVA反序列化
        CVE-2016-0638  
        CVE-2016-3510   
        CVE-2017-3248   
        CVE-2018-2628 
        CVE-2018-2893
        CVE-2019-2725
        CVE-2019-2729
        
        #任意文件上传
        CVE-2018-2894   
        
        #XMLDecoder反序列化
        CVE-2017-3506
        CVE-2017-10271 
        
	V 2.1更新日志：
    系列重新定义为WeblogicScanLot版本。
    新增大量成熟POC，与V1.3保持一致。
    同样新版本完全舍弃Python2。
    日志功能重构，更加健壮实用。
    Kill旧版本window下多进程适应性BUG


    【软件使用Demo】
	【此处只提供了本机单机扫描demo，多线程实战场面太过血腥，请在家长陪同下自行体验】
	
	#控制台：
    =========================================================================
	__        __   _     _             _        ____
	\ \      / /__| |__ | | ___   __ _(_) ___  / ___|  ___ __ _ _ __
	 \ \ /\ / / _ \ '_ \| |/ _ \ / _` | |/ __| \___ \ / __/ _` | '_ \
	  \ V  V /  __/ |_) | | (_) | (_| | | (__   ___) | (_| (_| | | | |
	   \_/\_/ \___|_.__/|_|\___/ \__, |_|\___| |____/ \___\__,_|_| |_|
	                             |___/
	                             By Tide_RabbitMask | V 2.1


	Welcome To WeblogicScan !!!
	Whoami：rabbitmask.github.io

	[*]任务加载成功，目标:127.0.0.1:7001

	[*]任务检测完成，目标:127.0.0.1:7001

	>>>>>End of task

    =========================================================================
	
	#日志文件：
    =========================================================================
	
	2019-07-08 21:11:48,385 [+]The target Weblogic console address is exposed! The path is: http://127.0.0.1:7001/console/login/LoginForm.jsp Please try weak password blasting!
	2019-07-08 21:11:48,385 [+]The target Weblogic UDDI module is exposed! The path is: http://127.0.0.1:7001/uddiexplorer/ Please verify the SSRF vulnerability!
	2019-07-08 21:11:48,385 [-]CVE_2016_0638 not detected.
	2019-07-08 21:11:48,385 [-]CVE_2016_3510 not detected.
	2019-07-08 21:11:48,385 [-]CVE_2017_3248 not detected.
	2019-07-08 21:11:51,024 [-]Target weblogic not detected CVE-2017-3506
	2019-07-08 21:11:51,044 [-]Target weblogic not detected CVE-2017-10271
	2019-07-08 21:11:51,044 [-]CVE_2018_2628 not detected.
	2019-07-08 21:11:51,044 [-]CVE_2018_2893 not detected.
	2019-07-08 21:11:51,054 [-]Target weblogic not detected CVE-2018-2894
	2019-07-08 21:11:51,563 [+]The target weblogic has a JAVA deserialization vulnerability:CVE-2019-2725
	2019-07-08 21:11:51,753 [+]Your current permission is:rabbitmask\rabbitmask
	2019-07-08 21:11:54,062 [+]The target weblogic has a JAVA deserialization vulnerability:CVE-2019-2729
	2019-07-08 21:11:54,062 [+]Your current permission is:  rabbitmask\rabbitmask

	=========================================================================
