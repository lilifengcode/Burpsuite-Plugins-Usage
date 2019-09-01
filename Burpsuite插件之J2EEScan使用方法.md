## ![2019-03-26_163135.png](https://image.3001.net/images/20190401/1554087200_5ca17d20890a2.png!small)

## **￥￥很久很久之前投过的，但是没收，，，，懒得重新搞了直接复制过来了 ##

## 一.burp suite插件之J2EEscan

### 1.J2EEScan介绍

J2EEScan是Burp Suite的插件。此插件的目标是在J2EE应用程序的Web应用程序渗透测试期间改进测试覆盖率。【官方】

J2EEScan能测漏洞，比如<span style="color: rgb(68, 68, 68);">Apache Struts</span>、<span style="color: rgb(68, 68, 68);">JBoss</span>、<span style="color: rgb(68, 68, 68);"><span style="color: rgb(68, 68, 68);">Java Server</span>、<span style="color: rgb(68, 68, 68);">Tom猫、等东东的漏洞。【非高大尚解释】</span></span>

_<span style="color: rgb(68, 68, 68);"><span style="color: rgb(68, 68, 68);">详细如下：</span></span>_

## 测试用例：

**杂项**

*   表达语言注入（CVE-2011-2730）
*   Apache Roller OGNL注射液（CVE-2013-4212）
*   本地文件包括 - /WEB-INF/web.xml已检索
*   本地文件包含 - 检索Spring应用程序上下文
*   本地文件包含 - 检索到struts.xml
*   本地文件包含 - 检索到weblogic.xml
*   本地文件包含 - 检索到的ibm-ws-bnd.xml
*   本地文件包含 - ibm-web-ext.xmi检索
*   本地文件包含 - 检索到的ibm-web-ext.xml
*   本地文件包含 - / etc / shadow已检索
*   本地文件包含 - / etc / passwd已检索
*   HTTP Auth弱密码
*   检索到WEB-INF应用程序配置文件
*   状态Servlet（CVE-2008-3273）
*   Snoop Servlet（CVE-2012-2170）
*   扩展路径遍历扫描
*   AJP服务检测 - 感谢[@ikki](https://twitter.com/_ikki)
*   弹簧启动执行器控制台
*   UTF8响应拆分
*   JK管理端点
*   Pivotal Spring Traversal（CVE-2014-3625）

**Apache Struts**

*   Apache Struts 2 S2-023 - 感谢[@ h3xstream](https://twitter.com/h3xstream)
*   Apache Struts 2 S2-016
*   Apache Struts 2 S2-017
*   Apache Struts 2 S2-020
*   Apache Struts 2 S2-021
*   Apache Struts 2 S2-032
*   Apache Struts DevMode已启用
*   Apache Struts OGNL控制台

**Grails的**

*   Grails Path Traversal（CVE-2014-0053）

**Apache Wicket**

*   Apache Wicket任意资源访问（CVE-2015-2080）

**Java Server Faces**

*   Java Server Faces本地文件包含（CVE-2013-3827 CVE-2011-4367）

**JBoss SEAM**

*   JBoss SEAM远程命令执行（CVE-2010-1871）

**错误处理不正确**

*   JSF
*   Apache Struts
*   Apache Tapestry
*   Grails的
*   GWT
*   Java的

**XML安全性**

*   X包括支持
*   XML外部实体

**信息披露问题**

*   远程JVM版本
*   Apache Tomcat版本
*   码头版
*   Oracle Application Server版本
*   Oracle Glassfish版本
*   Oracle Weblogic版本

**合规性检查**

*   web.xml - HTTP动词篡改
*   web.xml - 会话跟踪的URL参数
*   web.xml - 不完整的错误处理
*   web.xml - Invoker Servlet

**JBoss**

*   JBoss Web服务枚举
*   JBoss管理员控制台弱密码
*   JBoss JMX / Web控制台不受密码保护
*   JBoss JMX Invoker远程命令执行
*   JBoss Undertow目录遍历（CVE-2014-7816）
*   JBoss jBPM管理控制台

**Tomcat**

*   Tomcat Manager控制台弱密码
*   Tomcat Host Manager控制台弱密码
*   生命终结软件 - Tomcat

**Weblogic**

*   Weblogic UDDI Explorer Detection
*   Weblogic UDDI Explorer SSRF漏洞（CVE-2014-4210）
*   Weblogic管理控制台弱密码

**Oracle应用服务器**

*   添加了对Oracle Log Database Accessible的检查
*   添加了对多个Oracle应用服务器默认资源的检查（CVE-2002-0565，CVE-2002-0568，CVE-2002-0569）
*   生命周期结束软件 - Oracle应用服务器

**码头**

*   由[@gdssecurity](https://twitter.com/gdssecurity/)发现的Jetty Remote Leak Shared Buffers（CVE-2015-2080）
*   生命终结软件 - 码头

**Apache Axis**

*   Apache Axis2 - Web服务枚举
*   Apache Axis2 - 管理控制台弱密码
*   Apache Axis2 - 本地文件包含漏洞（OSVDB 59001）
*   Apache Axis2 - Happy Axis

**NodeJS**

*   NodeJS HTTP重定向（CVE-2015-1164）
*   NodeJS HTTP响应拆分（CVE-2016-2216）

### <span style="color: rgb(68, 68, 68);"><span style="color: rgb(68, 68, 68);"></span></span>2.J2EEScan安装

* 从“选项” - >“会话”中的“Cookie jar”部分启用扫描程序字段

* 在Burp Extender选项卡中加载J2EEscan jar

* 该插件至少需要Java 1.7

**1) Cookie Jar启动扫描程序**

Burp通过维护Cookie jar来维护你访问过得所有web站点的cookie信息，Cookie jar的信息在Burp的所有工具组件之间是数据共享的。

![2019-04-01_150901.png](https://image.3001.net/images/20190401/1554102606_5ca1b94e7606f.png!small)我们可以通过上图中的勾选项配置，来指定Cookie jar在哪些工具组件之间生效。

**2) 下载安装J2EEScan**

在Burp Extender选项卡中，找到J2EEscan jar**，**点击**install**进行安装

![2019-04-01_151236.png](https://image.3001.net/images/20190401/1554102819_5ca1ba2358542.png!small)**3）java版本至少为1.7**

运行Java -version 检测

![2019-04-01_151529.png](https://image.3001.net/images/20190401/1554103019_5ca1baeb93761.png!small)

### 3.搭建测试环境【S2-016]等

_找了好多集成测试平台，都不合适，只能用vulhub自己搭建一个了。_

_关于具体搭建方法可以参考[vulhub官网](https://vulhub.org/)，有视频有文档。
_

**kali 下搭建 ：
第一步：执行命令 sudo apt  install docker.io**

![2019-04-01_211301.png](https://image.3001.net/images/20190401/1554124646_5ca20f66975d5.png!small)**碰到y/n  或者 yes / not   一律yes **

![2019-04-01_211340.png](https://image.3001.net/images/20190401/1554124659_5ca20f7339b86.png!small)**第二步：检测docker是否安装成功，命令行执行：docker -v
![2019-04-01_212527.png](https://image.3001.net/images/20190401/1554125206_5ca21196624a8.png!small)****第三步：启动docker,命令行执行：sudo service  docker  start
              查看是否启动成功执行：sudo service docker status,running代表启动成功**

![2019-04-01_212431.png](https://image.3001.net/images/20190401/1554125354_5ca2122a9e100.png!small)**第四步：安装docker-compose ,执行命令：pip install docker-compose
 我这之前装过already
**

**![2019-04-01_213238.png](https://image.3001.net/images/20190401/1554125577_5ca21309c93ee.png!small)
<span></span>**

**第五步：安装下载vulhub,执行命令： git clone [https://github.com/vulhub/vulhub.git](https://github.com/vulhub/vulhub.git)![2019-04-01_213552.png](https://image.3001.net/images/20190401/1554125775_5ca213cfc734b.png!small)****_我这个随便搞得，建议git clone 的时候，在/tmp目录下执行【安装过程慢得很啊】
_
第六步：安装好后进入到vulhub,目录，选择一个你想创建使用的漏洞执行：docker-compose up -d 即可
![2019-04-01_214211.png](https://image.3001.net/images/20190401/1554126257_5ca215b1c614b.png!small)****执行完就等着吧，，，慢的很**
![2019-04-01_214608.png](https://image.3001.net/images/20190401/1554126386_5ca21632c0dc6.png!small)

### 4.使用演示

**1) 访问漏洞地址：[http://192.168.6.145:8080/index.action?](http://192.168.6.145:8080/index.action?)**

![2019-04-01_220425.png](https://image.3001.net/images/20190401/1554127574_5ca21ad68acdc.png!small)**2) 为确定是否成功搭建环境，我们事先用工具验证一下是否存在s2-016**

![2019-04-01_220715.png](https://image.3001.net/images/20190401/1554127663_5ca21b2fca097.png!small)**3) 打开burp suite,进行抓包，并扫描网站**

![2019-04-01_220252.png](https://image.3001.net/images/20190401/1554127751_5ca21b87220ee.png!small)**4)切换到scanner 里面观察，等待**

![2019-04-01_221847.png](https://image.3001.net/images/20190401/1554128394_5ca21e0aeddf6.png!small)**这里面扫出来的是S2-017,其实是没扫完，在Scan queue队列可以看到只扫了33%**

### ![2019-04-01_222037.png](https://image.3001.net/images/20190401/1554128497_5ca21e71eb209.png!small)

### 5.注意事项

1）使用前，请确保cookier jar里面选择scanner

2) J2EEScan,并不像其他 插件一样有单独的菜单

### ![2019-04-02_094025.png](https://image.3001.net/images/20190402/1554169351_5ca2be0755580.png!small)

### 参考链接：[https://t0data.gitbooks.io/burpsuite/content/chater14.html   [COOKIER JAR释义参考出处】


###                   [https://github.com/portswigger/j2ee-scan](https://github.com/portswigger/j2ee-scan)